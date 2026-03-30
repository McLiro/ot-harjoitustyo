import pygame

class State():
    def __init__(self, game):
        self.done = False
        self.next_state = None
        self.game = game


    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()

        for element in self.ui_elements:
            if hasattr(element, 'update'):
                element.update(mouse_pos)

        for ship in self.ships:
            if hasattr(ship, 'update'):
                ship.update(mouse_pos)


    def draw(self, screen):
        for element in self.ui_elements:
            element.draw(screen)

        for ship in self.ships:
            ship.draw(screen)
