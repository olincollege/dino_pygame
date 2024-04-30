"""
This module contains unit tests for the Cactus class defined in the `cactus`
module.
"""

import pytest
import pygame
from cactus import Cactus


# pylint: disable=redefined-outer-name
@pytest.fixture
def setup_cactus():
    """Setup fixture for creating a cactus instance."""
    pygame.init()  # pylint: disable=no-member
    screen = pygame.display.set_mode((800, 600))
    return Cactus(screen, 800, 600)


def test_cactus_initialization(setup_cactus):
    """Test the initialization of the cactus."""
    cactus = setup_cactus
    assert cactus.rect.x == 800
    assert cactus.rect.y == 600 - cactus.rect.height


def test_cactus_update(setup_cactus):
    """Test the cactus movement."""
    cactus = setup_cactus
    initial_x = cactus.rect.x
    cactus.update(10)
    assert cactus.rect.x == initial_x - 10

    cactus.rect.right = -1
    cactus.update(10)
    assert cactus.rect.x < 0


def test_cactus_draw(setup_cactus):
    """Test the drawing of the cactus."""
    cactus = setup_cactus
    cactus.draw()
    assert True
