import pygame

class Renderer():
    def __init__(self, screen):
        self.screen = screen

    def render(self, state):
        self.screen.fill((30, 30, 30))

        state.draw(self.screen)

        pygame.display.flip()