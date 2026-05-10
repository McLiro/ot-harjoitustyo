import sqlite3
import json
from pathlib import Path
from datetime import datetime
from logic.board_logic import BoardLogic

DB_PATH = Path(__file__).parent.parent / "data" / "saves.db"

class GameDatabase:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA foreign_keys=ON;")
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS saved_games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    board_size INTEGER NOT NULL,
                    player_board TEXT NOT NULL,
                    ai_board TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    last_played_at TEXT NOT NULL
                )
            """)

    def save_new(self, board_size: int, player_board: BoardLogic,
                ai_board: BoardLogic, difficulty: str):
        player_board_json = json.dumps(player_board.to_dict())
        ai_board_json = json.dumps(ai_board.to_dict())
        time_now = datetime.now().isoformat()

        with self._get_conn() as conn:
            cur = conn.execute(
                """INSERT INTO saved_games
                (board_size, player_board, ai_board, difficulty, last_played_at)
                VALUES (?, ?, ?, ?, ?)""",
                (board_size, player_board_json, ai_board_json, difficulty, time_now)
            )
            return cur.lastrowid

    def update(self, player_board: BoardLogic, ai_board: BoardLogic, save_id: int):
        player_board_json = json.dumps(player_board.to_dict())
        ai_board_json = json.dumps(ai_board.to_dict())
        time_now = datetime.now().isoformat()

        with self._get_conn() as conn:
            conn.execute(
                "UPDATE saved_games SET player_board=?, ai_board=?, last_played_at=? WHERE id=?",
                (player_board_json, ai_board_json, time_now, save_id)
            )

    def load(self, save_id: int):
        with self._get_conn() as conn:
            row = conn.execute("SELECT * FROM saved_games WHERE id=?", (save_id,)).fetchone()
            if not row:
                return None

            player_data = json.loads(row["player_board"])
            ai_data = json.loads(row["ai_board"])
            difficulty = row["difficulty"]

            player_board = BoardLogic.from_dict(player_data)
            ai_board = BoardLogic.from_dict(ai_data)

            player_board.save_id = ai_board.save_id = row["id"]

            return player_board, ai_board, difficulty

    def list_saves(self):
        with self._get_conn() as conn:
            return [dict(r) for r in conn.execute(
                "SELECT id, last_played_at FROM saved_games ORDER BY last_played_at DESC"
            ).fetchall()]

    def delete(self, save_id: int):
        with self._get_conn() as conn:
            conn.execute("DELETE FROM saved_games WHERE id=?", (save_id,))
