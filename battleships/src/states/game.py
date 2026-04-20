import pygame
from sprites.ui import Grid, Ship
from logic.board_logic import BoardLogic
from .base import State

class Game(State):
    def __init__(self, game, board: BoardLogic):
        super().__init__(game)

        self.player_board = board
        self.ai_board = BoardLogic(10)
        self.ai_board.generate_board([5, 4, 3, 3, 2])

        white = pygame.Color('white')
        self.grid_size = 50
        self.player_grid = Grid(50, 50, self.grid_size, white)
        self.ai_grid = Grid(750, 50, self.grid_size, white)

        self.ui_elements = [self.player_grid,
                            self.ai_grid]

        self.ships = []
        self.placed_ships = [] # PLAYER SHIPS

        self.set_player_ships()

    def handle_events(self, events):
        pass

    def update_board(self, board: BoardLogic):
        pass

    def get_coords(self, mouse_pos):
        mouse_x = mouse_pos[0] - 750
        mouse_y = mouse_pos[1] - 50

        return (mouse_x // self.grid_size, mouse_y // self.grid_size)


    def get_pixels(self, x, y):
        return (750 + x * self.grid_size, 50 + y * self.grid_size)

    def set_player_ships(self):

        def get_pixels(x, y):
            return (50 + x * self.grid_size, 50 + y * self.grid_size)

        for ship in self.player_board.ships:
            x, y = get_pixels(ship.x, ship.y)
            length = ship.length
            rotation = ship.rotation

            if rotation == "H":
                ship = Ship(x, y, length, 1, 50)
            else:
                ship = Ship(x, y, 1, length, 50)

            self.placed_ships.append(ship)
