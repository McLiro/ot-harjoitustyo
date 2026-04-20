import pygame
from .base import State
from sprites.ui import Grid
from logic.board_logic import BoardLogic

class Game(State):
    def __init__(self, game, board: BoardLogic):
        super().__init__(game)

        self.board = board

        white = pygame.Color('white')
        grid_size = 50
        self.player_grid = Grid(50, 50, grid_size, white)
        self.ai_grid = Grid(750, 50, grid_size, white)

        self.ui_elements = [self.player_grid,
                            self.ai_grid]

        self.ships = []
        self.placed_ships = []

    def handle_events(self, events):
        pass

    def update_board(self, board: BoardLogic):
        pass
