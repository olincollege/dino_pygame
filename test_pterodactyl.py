"""
This module contains unit tests for the Pterodactyl class defined in the
`pterodactyl` module.
"""

import pytest
import pygame
from pterodactyl import Pterodactyl


# pylint: disable=redefined-outer-name
@pytest.fixture
def pterodactyl_setup():
    """Setup Pygame and create a screen to pass to the Pterodactyl class."""
    pygame.init()  # pylint: disable=no-member
    screen = pygame.display.set_mode((800, 600))
    return Pterodactyl(screen, 800, 600, 100)


def test_pterodactyl_initialization(pterodactyl_setup):
    """Test the Pterodactyl initialization sets correct initial position."""
    assert pterodactyl_setup.rect.x == 800
    assert pterodactyl_setup.rect.y == 100


def test_pterodactyl_update(pterodactyl_setup):
    """Test the update method decreases x position correctly."""
    initial_x = pterodactyl_setup.rect.x
    pterodactyl_setup.update(5)
    assert pterodactyl_setup.rect.x == initial_x - 5
    pterodactyl_setup.rect.right = -10
    pterodactyl_setup.update(5)
    assert pterodactyl_setup.rect.x < 0


def test_pterodactyl_animation(pterodactyl_setup):
    """Test that the animation frame updates correctly and loops."""
    initial_frame = pterodactyl_setup.animation_frame
    for _ in range(100):
        pterodactyl_setup.draw_ptero()
    assert pterodactyl_setup.animation_frame != initial_frame
    assert pterodactyl_setup.animation_frame < len(pterodactyl_setup.images)
