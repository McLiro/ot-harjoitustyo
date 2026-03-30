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

    engine.state_dict["MOCK"] = mock_state

    engine.state.done = True
    engine.state.next_state = "MOCK"

    engine.change_state()

    assert engine.state == mock_state

def test_quit_event():
    engine = GameEngine()
    mock_event = MagicMock
    mock_event.type = pygame.QUIT

    engine._handle_events([mock_event])

    assert engine.running is False
