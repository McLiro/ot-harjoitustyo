import os
import pytest
from unittest.mock import MagicMock
import pygame

os.environ['SDL_VIDEODRIVER'] = 'dummy'

from engine import GameEngine

@pytest.fixture(autouse=True)
def init_dummy_pygame():
    pygame.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()

def test_init():
    engine = GameEngine()

    assert engine.running is True

def test_change_state():
    engine = GameEngine()
    mock_state = MagicMock()

    engine.state.done = True
    engine.state.next_state = mock_state

    engine.change_state()

    assert engine.state == mock_state

def test_quit_event():
    engine = GameEngine()
    mock_event = MagicMock()
    mock_event.type = pygame.QUIT

    engine._handle_events([mock_event])

    assert engine.running is False