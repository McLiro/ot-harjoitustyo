import pygame

class Ship:
    def __init__(self, x, y, width, height, cell_size, visible: bool=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = 3
        self.visible = visible

        self.cell_size = cell_size
        self.rect = pygame.Rect(x, y, width * cell_size, height * cell_size)

        self.color = pygame.color.Color('steelblue2')
        self.hover_color = pygame.color.Color('steelblue3')
        self.selected_color = pygame.color.Color('limegreen')
        self.placed_color = pygame.color.Color('gray40')
        self.current_color = pygame.color.Color('steelblue2')

        self.placed = False
        self.selected = False

    
    def border_color(self, color):
        return tuple(max(0, int(c * 0.6)) for c in color)


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
        if self.visible:
            pygame.draw.rect(screen, self.current_color, self.rect)

            border_color = self.border_color(self.current_color)
            pygame.draw.rect(screen, border_color, self.rect, self.border_width)
