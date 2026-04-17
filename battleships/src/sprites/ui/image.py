import os
import pygame

class Image():
    def __init__(self, x, y, angle, filename):

        self.rect_center = (x, y)

        self.asset = pygame.image.load(self.get_asset_path(filename)).convert_alpha()

        self.rotate(angle)

    def get_asset_path(self, filename):
        base_dir = os.path.dirname(__file__)
        return os.path.join(base_dir, "assets", filename)
    
    def rotate(self, new_angle):
        self.image = pygame.transform.rotate(self.asset, new_angle)
        self.rect = self.image.get_rect(center=self.rect_center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)