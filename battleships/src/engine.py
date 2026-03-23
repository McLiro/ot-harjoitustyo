import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, CAPTION
from renderer import Renderer

class GameEngine():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True

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
            self.state.handle_events(event)

    def _update(self, dt):
        self.state.update(dt)

    def _render(self):
        self.renderer.render(self.screen, self.state)