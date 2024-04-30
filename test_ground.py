"""
This module contains unit tests for the Ground class defined in the `ground`
module.
"""

from unittest.mock import Mock, patch
import pytest
import pygame
from ground import Ground


# pylint: disable=redefined-outer-name
@pytest.fixture
def setup_ground():
    """Setup fixture for creating a ground instance."""
    pygame.init()  # pylint: disable=no-member
    screen = Mock(spec=pygame.Surface)
    image = pygame.Surface((200, 20))
    with patch("pygame.image.load", return_value=image):
        ground = Ground(800, 600, screen, "path/to/image.png")
    return ground, screen


def test_ground_initialization(setup_ground):
    """Test the initialization of the ground."""
    ground, _ = setup_ground
    assert ground.rect.y == 600 - 20
    assert ground.x_1 == 0
    assert ground.x_2 == 200


def test_ground_update(setup_ground):
    """Test the ground's movement and wrap-around functionality."""
    ground, _ = setup_ground
    initial_x1 = ground.x_1
    initial_x2 = ground.x_2

    ground.update(10)
    assert ground.x_1 == initial_x1 - 10
    assert ground.x_2 == initial_x2 - 10

    ground.x_1 = -200
    ground.update(10)
    assert ground.x_1 == ground.x_2 + 200


def test_ground_draw(setup_ground):
    """Test the drawing functionality of the ground."""
    ground, mock_surface = setup_ground
    ground.draw_ground()

    assert mock_surface.blit.call_count == 2


def test_ground_get_rect(setup_ground):
    """Test the functionality of getting the ground's rect."""
    ground, _ = setup_ground
    rect = ground.get_rect()
    assert rect.top == ground.rect.y
    assert rect.width == 800
    assert rect.height == 60
