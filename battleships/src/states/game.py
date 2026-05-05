import pygame
from sprites.ui import Grid, Ship, HitMarker
from logic import BoardLogic, ShipLogic, Easy, Medium
from .base import State

class Game(State):
    def __init__(self, game, board: BoardLogic, difficulty: str):
        super().__init__(game)

        self.difficulty = difficulty
        self.player_board = board
        self.ai_board = BoardLogic(10)
        self.ai_board.generate_board([5, 4, 3, 3, 2])
        self.ai_logic = self.start_ai_logic(self.player_board, self.difficulty)

        white = pygame.Color('white')
        self.grid_size = 50
        self.player_grid = Grid(50, 50, self.grid_size, white)
        self.ai_grid = Grid(750, 50, self.grid_size, white)

        self.ui_elements = [self.player_grid,
                            self.ai_grid]
        
        self.hitmarkers = []

        self.sunk_ships = []

        self.ships = self.set_ships(self.ai_board, True) # AI SHIPS
        self.placed_ships = self.set_ships(self.player_board, False) # PLAYER SHIPS

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = self.get_coords(event.pos)
                pixels = self.get_ai_grid_pixels(coords[0], coords[1])
                self.handle_shooting(coords, pixels)

    def handle_shooting(self, coords, pixels):
        impact = self.ai_board.validate_shot(coords)

        if impact is False:
            return

        result = impact[0]
        print(result, flush=True)

        if result == "MISS":
            self.hitmarkers.append(HitMarker(pixels[0], pixels[1], False))
        elif result == "HIT":
            self.hitmarkers.append(HitMarker(pixels[0], pixels[1], True))
        elif result == "SUNK":
            ship = impact[1]
            x, y = self.get_ai_grid_pixels(ship.x, ship.y)
            ship_sprite = ship.create_sprite(x, y)
            ship_sprite.current_color = pygame.Color('red')
            self.sunk_ships.append(ship_sprite)

        self.ai_move()

    def ai_move(self):
        pass

    def get_coords(self, mouse_pos):
        mouse_x = mouse_pos[0] - 750
        mouse_y = mouse_pos[1] - 50

        return (mouse_x // self.grid_size, mouse_y // self.grid_size)


    def get_ai_grid_pixels(self, x, y):
        return (750 + x * self.grid_size, 50 + y * self.grid_size)
    
    def get_player_grid_pixels(self, x, y):
        return (50 + x * self.grid_size, 50 + y * self.grid_size)

    def set_ships(self, board, is_ai: bool):
        placements = []

        for ship in board.ships:
            if is_ai:
                x, y = self.get_ai_grid_pixels(ship.x, ship.y)
            else:
                x, y = self.get_player_grid_pixels(ship.x, ship.y)

            ship_sprite = ship.create_sprite(x, y)

            if is_ai:
                ship_sprite.visible = False

            placements.append(ship_sprite)

        return placements

    def start_ai_logic(self, board, difficulty):
        if difficulty == "easy":
            return Easy(board)
        if difficulty == "medium":
            return Medium(board)