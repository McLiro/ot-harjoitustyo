import pygame

class Grid:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.grid = self.create_grid()

    
    def create_grid(self):
        grid = []

        for row in range(10):
            for col in range(10):
                x = self.x + (col * self.size)
                y = self.y + (row * self.size)

                grid.append(pygame.Rect(x, y, self.size, self.size))

        return grid


    def draw(self, screen):
        for rect in self.grid:
            pygame.draw.rect(screen, self.color, rect, 1)
