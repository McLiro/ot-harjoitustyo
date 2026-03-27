import unittest
import pytest
from unittest.mock import MagicMock, patch
import pygame
from engine import GameEngine


@pytest.fixture(autouse=True)
def mock_pygame():
    with patch('pygame.display.set_mode'), \
         patch('pygame.display.set_caption'), \
         patch('pygame.font.init'), \
         patch('pygame.font.Font'):
        
        pygame.init()
        yield
        pygame.quit()

def test_init():
    engine = GameEngine()

    assert engine.running is True

def test_change_state():
    engine = GameEngine()
    mock_state = MagicMock()

    engine.change_state(mock_state)
    mock_state.assert_called_once_with(engine)

def test_quit_event():
    engine = GameEngine()
    mock_event = MagicMock
    mock_event.type = pygame.QUIT

    engine._handle_events([mock_event])

    assert engine.running is False