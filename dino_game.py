"""
Main program to setup and run the dino game
"""

import pygame
from dino_game_controller import KeyboardDinoGameController
from dino_game_controller import CameraDinoGameController
from dino_game_model import DinoGame
from dino_game_view import DinoGameView


def main():
    """
    Setup and play dino game using MVC architecture.
    """
    pygame.init()  # pylint: disable=no-member
    game = DinoGame()
    game_view = DinoGameView(game)
    camera_player = CameraDinoGameController(game)
    keyboard_player = KeyboardDinoGameController(game)
    while game.running and game.is_intro:  # intro screen
        keyboard_player.get_input()
        game_view.draw_intro()
    while game.running:  # main game loop
        keyboard_player.get_input()
        camera_player.get_input()
        if not game.game_over:
            game.update()
            game_view.update_view()
        else:  # Game over screen
            keyboard_player.get_restart()
            camera_player.get_restart()
            game_view.show_end_screen()

    pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    main()
