import pygame
from .base import State

class GameOver(State):
    def __init__(self, game, winner):
        super().__init__(game)
        self.winner = winner

    def handle_events(self, events):
        for event in events:
            pass