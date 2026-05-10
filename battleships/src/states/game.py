import pygame
from sprites.ui import Grid, HitMarker, Button
from logic import BoardLogic, Easy, Medium
from db.db import GameDatabase
from .base import State
from .game_over import GameOver

class Game(State):
    def __init__(self, game, player_board: BoardLogic=None,
                difficulty: str=None, save_file_id: int=None):
        super().__init__(game)

        self.game = game
        self.database = GameDatabase()

        white = pygame.Color('white')
        self.grid_size = 50
        self.player_grid = Grid(50, 50, self.grid_size, white)
        self.ai_grid = Grid(750, 50, self.grid_size, white)
        self.main_menu_button = Button(650, 625, 200, 100, "MAIN MENU", white,
                                       pygame.Color('whitesmoke'), pygame.Color('black'),
                                       pygame.font.Font(None, 30), True)

        self.ui_elements = [self.player_grid,
                            self.ai_grid,
                            self.main_menu_button]

        self.hitmarkers = []

        self.sunk_ships = []

        if save_file_id is None:
            self.new_game(player_board, difficulty)
        else:
            self.load_game(save_file_id)

        self.set_hitmarkers()
        self.ships = self.set_ships(self.ai_board, True) # AI SHIPS
        self.placed_ships = self.set_ships(self.player_board, False) # PLAYER SHIPS

    def load_game(self, save_file_id):
        self.player_board, self.ai_board, self.difficulty = self.database.load(save_file_id)

        self.ai_logic = self.start_ai_logic(self.difficulty)

        for shot in self.player_board.shots:
            self.ai_logic.unshot_coords.remove(shot)

    def new_game(self, player_board, difficulty):
        self.player_board = player_board
        self.difficulty = difficulty

        self.ai_board = BoardLogic(10)
        self.ai_board.generate_board([5, 4, 3, 3, 2])
        self.ai_logic = self.start_ai_logic(self.difficulty)

        self.player_board.save_id = self.ai_board.save_id = self.database.save_new(
        10, self.player_board, self.ai_board, difficulty)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.main_menu_button.rect.collidepoint(event.pos):
                    from .menu import Menu
                    self.next_state = Menu(self.game)
                    self.done = True

                coords = self.get_coords(event.pos)
                pixels = self.get_ai_grid_pixels(coords[0], coords[1])
                self.handle_shooting(coords, pixels)

    def game_over(self, is_ai: bool):
        if is_ai:
            self.next_state = GameOver(self.game, "AI")
        else:
            self.next_state = GameOver(self.game, "PLAYER")

        self.database.delete(self.player_board.save_id)
        self.done = True

    def handle_shooting(self, coords, pixels):
        impact = self.ai_board.validate_shot(coords)

        if impact is False:
            return

        result = impact[0]

        self.draw_hitmarker(pixels, result)

        if result == "SUNK":
            ship = impact[1]
            x, y = self.get_ai_grid_pixels(ship.x, ship.y)
            ship_sprite = ship.create_sprite(x, y)
            ship_sprite.current_color = pygame.Color('red')
            self.sunk_ships.append(ship_sprite)

        if self.ai_board.has_lost():
            self.game_over(is_ai=False)

        self.ai_move()

        if self.player_board.has_lost():
            self.game_over(is_ai=True)

    def ai_move(self):
        target = self.ai_logic.make_move()
        pixels = self.get_player_grid_pixels(target[0], target[1])

        impact = self.player_board.validate_shot(target)
        result = impact[0]

        self.draw_hitmarker(pixels, result)

        self.ai_logic.process_result(target, result)

        if result == "SUNK":
            ship = impact[1]
            x, y = self.get_player_grid_pixels(ship.x, ship.y)
            ship_sprite = ship.create_sprite(x, y)
            ship_sprite.current_color = pygame.Color('red')
            self.sunk_ships.append(ship_sprite)
            coords = []
            if ship.rotation == "H":
                for i in range(ship.length):
                    coords.append((ship.x + i, ship.y))
            else:
                for i in range(ship.length):
                    coords.append((ship.x, ship.y + i))

            self.ai_logic.process_sinking(coords)

        self.database.update(self.player_board, self.ai_board, self.player_board.save_id)

    def set_hitmarkers(self):
        # Player's shots drawn on the AI grid (right side)
        for shot in self.ai_board.shots:
            pixels = self.get_ai_grid_pixels(shot[0], shot[1])
            target = self.ai_board.grid[shot[1]][shot[0]]
            result = "HIT" if target is not None else "MISS"
            self.draw_hitmarker(pixels, result)

        # AI's shots drawn on the player grid (left side)
        for shot in self.player_board.shots:
            pixels = self.get_player_grid_pixels(shot[0], shot[1])
            target = self.player_board.grid[shot[1]][shot[0]]
            result = "HIT" if target is not None else "MISS"
            self.draw_hitmarker(pixels, result)

    def draw_hitmarker(self, pixels, result):
        if result == "HIT":
            self.hitmarkers.append(HitMarker(pixels[0], pixels[1], True))
        elif result == "MISS":
            self.hitmarkers.append(HitMarker(pixels[0], pixels[1], False))

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

            if is_ai and ship.is_sunk is False:
                ship_sprite.visible = False

            if ship.is_sunk:
                ship_sprite.current_color = pygame.Color('red')
                self.sunk_ships.append(ship_sprite)
            else:
                placements.append(ship_sprite)

        return placements

    def start_ai_logic(self, difficulty):
        if difficulty == "easy":
            return Easy()
        if difficulty == "medium":
            return Medium()
