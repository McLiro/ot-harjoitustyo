import pygame
from sprites.ui import Grid, Ship, Label
from .base import State
from logic.board_logic import BoardLogic
from logic.ship_logic import ShipLogic


class Start(State):
    def __init__(self, game):
        super().__init__(game)

        self.board = BoardLogic(10)

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

        self.placed_ships = []

        self.selected = None
        self.rotation = "H"


    def handle_events(self, events):
        # SELECTION
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.selected is not None:
                    length = self.selected.width
                    coords = self.get_coords(event.pos)

                    selected_ship = ShipLogic(coords[0], coords[1], length, self.rotation)

                    if self.board.place_ship(selected_ship):
                        pixels = self.get_pixels(coords[0], coords[1])
                        if self.rotation == "H":
                            new_sprite = Ship(pixels[0], pixels[1], length, 1, self.grid_size)
                        else:
                            new_sprite = Ship(pixels[0], pixels[1], 1, length, self.grid_size)

                        self.placed_ships.append(new_sprite)
                        self.selected.placed = True

                    else:
                        self.selected = None

                clicked_ship = None

                for ship in self.ships:
                    if ship.rect.collidepoint(event.pos):
                        clicked_ship = ship
                        break

                for ship in self.ships:
                    ship.selected = ship == clicked_ship

                self.selected = clicked_ship

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.rotation == "V":
                        self.rotation = "H"
                    else:
                        self.rotation = "V"


    def get_coords(self, mouse_pos):
        mouse_x = mouse_pos[0] - 50
        mouse_y = mouse_pos[1] - 50

        return (mouse_x // self.grid_size, mouse_y // self.grid_size)
    

    def get_pixels(self, x, y):
        return (50 + x * self.grid_size, 50 + y * self.grid_size)
