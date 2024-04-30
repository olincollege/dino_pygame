"""
Test DinoGameView class
"""

from dino_game_view import DinoGameView
from dino_game_model import DinoGame


# Create a mock DinoGame object


def test_dino_game_view_init():
    """
    Test class initialization
    """
    # Arrange
    mock_game = DinoGame()

    # Act
    view = DinoGameView(mock_game)

    # Assert
    assert view._game == mock_game  # pylint: disable=protected-access


def test_dino_game_view_draw_intro():
    """
    Test drawing the intro
    """
    # Arrange
    mock_game = DinoGame()
    view = DinoGameView(mock_game)

    # Act
    view.draw_intro()
    assert mock_game.window.get_size() == (791, 201)

    # Assert
    # Add your assertions here


def test_dino_game_view_update_view():
    """
    Test updating the view
    """
    # Arrange
    mock_game = DinoGame()
    view = DinoGameView(mock_game)

    # Act
    view.update_view()
    assert mock_game.window.get_size() == (791, 201)

    # Assert
    # Add your assertions here


def test_dino_game_view_show_end_screen():
    """
    Test displaying the game over screen
    """
    # Arrange
    mock_game = DinoGame()
    view = DinoGameView(mock_game)

    # Act
    view.show_end_screen()
    assert mock_game.window.get_size() == (791, 201)
