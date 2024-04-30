"""
This module contains unit tests for the Player class defined in the `player`
module.
"""

from unittest.mock import Mock
import pytest
import pygame
from player import Player


# pylint: disable=redefined-outer-name
@pytest.fixture
def setup_player():
    """Setup fixture for creating a Player instance."""
    pygame.init()  # pylint: disable=no-member
    screen = pygame.display.set_mode((800, 600))
    player = Player(screen, 800, 600)
    return player


def test_player_initialization(setup_player):
    """Test the initialization of the player."""
    player = setup_player
    assert player.rect.x == 0
    assert player.rect.y == 0


def test_player_jump(setup_player):
    """Test the player's jump functionality."""
    player = setup_player
    ground = Mock()
    ground.get_rect.return_value = pygame.Rect(0, 580, 800, 20)

    player.rect.bottom = ground.get_rect().top
    player.jump(ground)
    assert player.speed[1] < 0


def test_player_duck_unduck(setup_player):
    """Test the player's duck and unduck functionality."""
    player = setup_player
    player.duck()
    assert player.is_ducking is True
    player.unduck()
    assert player.is_ducking is False


def test_player_update(setup_player):
    """Test the update method which handles animation and movement."""
    player = setup_player
    ground = Mock()
    ground.get_rect.return_value = pygame.Rect(0, 580, 800, 20)

    player.rect.bottom = ground.get_rect().top - 10
    player.update(ground)
    assert player.speed[1] >= 0.5


def test_player_draw(setup_player):
    """Test the drawing functionality."""
    player = setup_player
    ground = Mock()
    ground.get_rect.return_value = pygame.Rect(0, 580, 800, 20)

    player.draw_player(ground)
    assert True
