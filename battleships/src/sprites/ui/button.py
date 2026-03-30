import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font, center=False):
        self.rect = pygame.Rect(x, y, width, height)

        if center:
             self.rect.center = (x, y)
        else:
             self.rect.topleft = (x, y)

        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = font

        self.text_surf = self.font.render(self.text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)