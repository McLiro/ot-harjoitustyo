import pygame
from sprites.ui import Label, Button
from .base import State

class GameOver(State):
    def __init__(self, game, winner):
        super().__init__(game)
        self.game = game
        self.label = self.winner_label(winner)
        self.new_game_button = Button(640, 350, 200, 100, "NEW GAME",
                                      pygame.Color('white'), pygame.Color('whitesmoke'),
                                      pygame.Color('black'), pygame.font.Font(None, 30), True)

        self.ui_elements = [
            self.label,
            self.new_game_button
        ]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game_button.rect.collidepoint(event.pos):
                    from .menu import Menu
                    self.next_state = Menu(self.game)
                    self.done = True

    def winner_label(self, winner):
        font = pygame.font.Font(None, 50)
        white = pygame.Color('white')
        if winner == "AI":
            return Label(640, 200, "You lost! Try again?", font, white)

        return Label(640, 200, "You won! New game?", font, white)
