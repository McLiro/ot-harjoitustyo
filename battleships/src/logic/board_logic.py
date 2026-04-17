class BoardLogic:
    def __init__(self, board_size):
        self.ships = []
        self.hits = []
        self.board_size = board_size
        self.grid = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_ship(self, ship):
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
        self.grid = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []