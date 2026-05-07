import sqlite3
from pathlib import Path
from datetime import datetime
from logic.board_logic import BoardLogic

DB_PATH = Path(__file__).parent.parent / "data" / "saves.db"

class GameDatabase:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def _get_conn(self):
        return sqlite3.connect(self.db_path)
    
    def _init_db(self):
        with self._get_conn as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS saved_games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    board_size INTEGER NOT NULL,
                    player_board TEXT NOT NULL,
                    ai_board TEXT NOT NULL,
                    last_played_at TEXT NOT NULL
                )
            """)

    def save_new(self, board_size: int, player_board: BoardLogic, ai_board: BoardLogic):
        player_board_json = player_board.to_dict()
        ai_board_json = ai_board.to_dict()
        time_now = datetime.now().isoformat()

        with self._get_conn as conn:
            cur = conn.execute(
                """INSERT INTO saved_games
                (board_size, player_board, ai_board, last_played_at)
                VALUES (?, ?, ?, ?)""",
                (board_size, player_board_json, ai_board_json, time_now)
            )
            return cur.lastrowid
