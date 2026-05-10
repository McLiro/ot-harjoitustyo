import pygame
from sprites.ui import Button, Label
from .base import State
from .game import Game

class Difficulty(State):
    def __init__(self, game, board):
        super().__init__(game)

        self.game = game
        self.board = board

        font = pygame.font.Font(None, 30)
        white = pygame.Color('white')
        whitesmoke = pygame.Color('whitesmoke')
        black = pygame.Color('black')

        self.label = Label(640, 200, "Choose difficulty:", font, white)
        self.easy = Button(640, 250, 200, 50, "EASY", white, whitesmoke, black, font, True)
        self.medium = Button(640, 310, 200, 50, "MEDIUM", white, whitesmoke, black, font, True)

        self.ui_elements = [
            self.label,
            self.easy,
            self.medium,
        ]

    def handle_events(self, events):
        difficulty = None

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.easy.rect.collidepoint(event.pos):
                    difficulty = "easy"
                if self.medium.rect.collidepoint(event.pos):
                    difficulty = "medium"

        if difficulty is not None:
            self.next_state = Game(self.game, self.board, difficulty)
            self.done = True
