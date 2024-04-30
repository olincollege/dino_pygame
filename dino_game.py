"""
Main program to setup and run the dino game
"""

from dino_game_controller import KeyboardDinoGameController
from dino_game_controller import CameraDinoGameController
from dino_game_model import DinoGame
from dino_game_view import DinoGameView
import pygame


def main():
    """
    Setup and play dino game using MVC architecture.
    """
    pygame.init()
    game = DinoGame()
    game_view = DinoGameView(game)
    camera_player = CameraDinoGameController(game)
    keyboard_player = KeyboardDinoGameController(game)
    while game.running:
        keyboard_player.get_input()
        camera_player.get_input()
        # first check if the game is over
        # check to see if the user quits
        # if the controller detects jumping inputes we should jimp
        # then if the controller detects ucking imputs ducks
        if not game.game_over:
            game.update()
            game_view.draw()
        else:
            keyboard_player.get_restart_click()
            game_view.show_end_screen()

    pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    main()
