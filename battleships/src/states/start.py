import pygame
from sprites.ui import Grid, Ship
from .base import State


class Start(State):
    def __init__(self, game):
        super().__init__(game)

        self.grid_size = 50
        self.white = pygame.color.Color('white')
        self.grid = Grid(50, 50, self.grid_size, self.white)

        self.ui_elements = [
            self.grid
        ]

        self.carrier = Ship(900, 50, 5, 1, self.grid_size)
        self.battleship = Ship(900, 150, 4, 1, self.grid_size)
        self.cruiser = Ship(900, 250, 3, 1, self.grid_size)
        self.submarine = Ship(900, 350, 3, 1, self.grid_size)
        self.destroyer = Ship(900, 450, 2, 1, self.grid_size)

        self.ships = [
            self.carrier,
            self.battleship,
            self.cruiser,
            self.submarine,
            self.destroyer
        ]

        self.selected = None


    def handle_events(self, events):
        # SELECTION
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_ship = None

                for ship in self.ships:
                    if ship.rect.collidepoint(event.pos):
                        clicked_ship = ship
                        break

                for ship in self.ships:
                    ship.selected = ship == clicked_ship

                self.selected = clicked_ship
