import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, CAPTION
from renderer import Renderer
from states import Menu, Start

class GameEngine():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)
        self.running = True
        self.state = Menu()

    def run(self):
        while self.running:
            dt = self._tick()
            events = pygame.event.get()
            self._handle_events(events)
            self._update(dt)
            self._render()

    def _tick(self):
        return self.clock.tick(FPS) / 1000.0
    
    def _handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.state.handle_events(events)

    def _update(self, dt):
        self.state.update(dt)

    def _render(self):
        self.renderer.render(self.state)