import pygame

class Ship:
    def __init__(self, x, y, width, height, cell_size):
        self.cell_size = cell_size
        self.rect = pygame.Rect(x, y, width * cell_size, height * cell_size)

        self.color = pygame.color.Color('steelblue2')
        self.hover_color = pygame.color.Color('steelblue3')
        self.selected_color = pygame.color.Color('limegreen')
        self.placed_color = pygame.color.Color('gray40')
        self.current_color = pygame.color.Color('steelblue2')

        self.placed = False
        self.selected = False


    def update(self, mouse_pos):
        if self.placed:
            self.current_color = self.placed_color
        elif self.selected:
            self.current_color = self.selected_color
        elif self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color


    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
