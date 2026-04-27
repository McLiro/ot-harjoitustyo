import pygame

class HitMarker():
    def __init__(self, x, y, on_target: bool):
        self.x = x + 25
        self.y = y + 25
        if on_target:
            self.color = pygame.Color('red')
        else:
            self.color = pygame.Color('royalblue')

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 23, 3)