import pygame

class Label:
    def __init__(self, x, y, text, font, color, center=True):
        self.font = font
        self.text = text
        self.color = color

        self.image = self.font.render(self.text, True, self.color)
        if center:
            self.rect = self.image.get_rect(center=(x, y))
        else:
            self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)