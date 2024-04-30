"""
Test DinoGameModel class
"""

import pytest
from dino_game import DinoGame


@pytest.fixture
def dino_game():
    """
    DinoGame fixture for testing
    """
    return DinoGame()


def test_dino_game_initialization(
    dino_game,
):  # pylint: disable=redefined-outer-name
    """
    Test the intialization step
    """
    assert dino_game.is_intro is True
    assert dino_game.running is True
    assert dino_game.game_over is False


def test_dino_game_restart(dino_game):  # pylint: disable=redefined-outer-name
    """
    Test Restarting the game
    """
    dino_game.restart()
    assert dino_game.game_over is False
    assert dino_game.score <= 0
    assert dino_game._speed >= 6  # pylint: disable=protected-access
    assert len(dino_game.pterodactyls) == 0
    assert len(dino_game.cacti) == 0
    assert dino_game.window.get_size() == (791, 201)


def test_dino_game_quit(dino_game):  # pylint: disable=redefined-outer-name
    """
    Test quiting out of the dino game
    """
    dino_game.quit()
    assert dino_game.running is False


def test_dino_game_start_game(
    dino_game,
):  # pylint: disable=redefined-outer-name
    """
    Test starting the game
    """
    dino_game.start_game()
    assert dino_game.is_intro is False


def test_dino_game_duck(dino_game):  # pylint: disable=redefined-outer-name
    """
    Test the ducking feature
    """
    dino_game.duck()
    # Check if the player is ducking
    assert dino_game.player.is_ducking is True


def test_dino_game_unduck(dino_game):  # pylint: disable=redefined-outer-name
    """
    Test the unducking feature
    """
    dino_game.unduck()
    # Check if the player is standing
    assert dino_game.player.is_ducking is False
