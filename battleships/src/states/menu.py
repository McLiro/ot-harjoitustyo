import pygame
from sprites.ui import Button, Label
from .base import State


class Menu(State):
    def __init__(self, game):
        super().__init__(game)

        self.title_font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 30)

        self.ui_elements = [
            Label(640, 30, "BATTLESHIPS", self.title_font, pygame.Color('white'), True), #TITLE
            Button(640, 300, 200, 100, "START", pygame.Color('white'),
                   pygame.Color('whitesmoke'), pygame.Color('black'),
                   self.button_font, True) #START BUTTON
        ]


    def handle_events(self, events):
        mouse_pos = pygame.mouse.get_pos()


    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()

        for element in self.ui_elements:
            if hasattr(element, 'update'):
                element.update(mouse_pos)


    def draw(self, screen):
        for element in self.ui_elements:
            element.draw(screen)
