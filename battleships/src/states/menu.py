import pygame
from sprites.ui import Button, Label
from .base import State


class Menu(State):
    def __init__(self, game):
        super().__init__(game)

        self.title_font = pygame.font.Font(None, 50)
        self.button_font = pygame.font.Font(None, 30)

        self.title = Label(640, 30, "BATTLESHIPS", self.title_font, pygame.Color('white'), True)
        self.start_button = Button(640, 300, 200, 100, "START", pygame.Color('white'),
                   pygame.Color('whitesmoke'), pygame.Color('black'),
                   self.button_font, True)

        self.ui_elements = [
            self.title,
            self.start_button
        ]


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.rect.collidepoint(event.pos):
                    self.next_state = "START"
                    self.done = True


    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()

        for element in self.ui_elements:
            if hasattr(element, 'update'):
                element.update(mouse_pos)


    def draw(self, screen):
        for element in self.ui_elements:
            element.draw(screen)
