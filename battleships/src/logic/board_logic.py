import random
from dataclasses import dataclass
from .ship_logic import ShipLogic

@dataclass
class BoardLogic:
    """Class for handling the game logic for placing down ships
    and keeping track of the state of the board.

    Attributes:
        ships: A list of ships on the game board.
        shots: A list of tuples representing shots.
        board_size: Variable for setting the size of the board.
        grid: Nested list, containing either a Ship class or None.
    """

    def __init__(self, board_size):
        """Constrctor for generating a new board.

        Args:
            board_size (int): Size of the board.
        """
        self.ships = []
        self.shots = []
        self.board_size = board_size
        self.grid = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        self.save_id = None

    def place_ship(self, ship):
        """Places down a ShipLogic class on the current board if possible.

        Args:
            ship (ShipLogic): An instance of the ShipLogic class.

        Returns:
            bool: True if ship placement is valid, False otherwise.
        """
        if self.can_place_ship(ship):
            self.ships.append(ship)

            for i in range(ship.length):
                if ship.rotation == "H":
                    self.grid[ship.y][ship.x + i] = ship
                else:
                    self.grid[ship.y + i][ship.x] = ship
            return True
        return False

    def can_place_ship(self, ship):
        """Checks if the ship placement is valid on the current board.

        Args:
            ship (ShipLogic): An instance of the ShipLogic class.

        Returns:
            bool: True if ship placement is valid, False otherwise.
        """
        potential_coords = []
        for i in range(ship.length):
            if ship.rotation == "H":
                nx, ny = ship.x + i, ship.y
            else:
                nx, ny = ship.x, ship.y + i
            potential_coords.append((nx, ny))

        for nx, ny in potential_coords:
            if nx < 0 or nx >= self.board_size or ny < 0 or ny >= self.board_size:
                return False

            if self.grid[ny][nx] is not None:
                return False

        return True

    def reset_board(self):
        """Resets the board back to a fully empty state.
        """
        self.grid = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []

    def generate_board(self, ship_lengths):
        """Creates a randomly generated board with valid ship placements.

        Args:
            ship_lengths (list[int]): A list of integers representing ship lenghts.
        """
        for length in ship_lengths:
            placed = False

            while not placed:
                ship = self.generate_ship(length)

                if self.place_ship(ship):
                    placed = True

    def generate_ship(self, length):
        """Randomly generates an instance of ShipLogic.

        Args:
            length (int): Length of the generated ship.

        Returns:
            ShipLogic: An instance of the ShipLogic class.
        """
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        rotation = random.choice(["H", "V"])
        return ShipLogic(x, y, length, rotation)

    def validate_shot(self, coords):
        x, y = coords
        if not (0 <= x <= 9 and 0 <= y <= 9):
            return False

        target = self.grid[y][x]

        if coords in self.shots:
            return False

        self.shots.append(coords)

        if target is not None:
            return target.hit(coords)

        return ("MISS", coords)

    def has_lost(self):
        for ship in self.ships:
            if ship.is_sunk is False:
                return False

        return True

    def to_dict(self):
        """Returns a dict of the board for JSON serialization."""
        ship_json = []
        for ship in self.ships:
            ship_json.append(ship.to_dict())

        return {
            "ships": ship_json,
            "shots": self.shots,
            "board_size": self.board_size
        }

    @classmethod
    def from_dict(cls, data: dict):
        board = cls(data["board_size"])
        board.ships = [ShipLogic.from_dict(s) for s in data["ships"]]
        board.shots = [tuple(shot) for shot in data["shots"]]
        board.grid = [[None for _ in range(board.board_size)] for _ in range(board.board_size)]
        for ship in board.ships:
            for i in range(ship.length):
                if ship.rotation == "H":
                    board.grid[ship.y][ship.x + i] = ship
                else:
                    board.grid[ship.y + i][ship.x] = ship
        return board
