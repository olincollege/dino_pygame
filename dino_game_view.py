"""
View for dino game
"""

import pygame
import math
import textwrap


class DinoGameView:
    """
    Creates a Dino Game view
    """

    pygame.init()
    _FONT_PATH = "PressStart2P-Regular.ttf"
    _FONT = pygame.font.Font(_FONT_PATH, 16)

    def __init__(self, DinoGame):
        """
        Initialize Dino Game view
        """

        self._game = DinoGame
        pygame.display.set_caption("Dino Game")

    def draw_intro(self):
        """
        Draw the intro screen/instructions
        """
        font = pygame.font.Font(self._FONT_PATH, 10)
        self._game.window.fill((255, 255, 255))
        self._game._ground.draw_ground()
        line_one = (
            "Welcome to the Chrome Dino Game… with a twist! To jump and duck,"
        )
        line_two = (
            " you need to physically move. Stand ~10 feet away from your camera"
        )
        line_three = "with it positioned at a 90 degree angle with the table. "
        line_four = (
            "There will be a 10 sec calibration period"
            "before obstacles start appearing."
        )
        line_five = "Space and down arrow can also be used."
        line_six = "Press space to begin calibration."
        text = [line_one, line_two, line_three, line_four, line_five, line_six]
        spacing = 0.1
        for index, line in enumerate(text):
            word_surface = font.render(line, 0, (0, 0, 0))
            word_rect = word_surface.get_rect(
                midtop=(
                    self._game.win_width / 2,
                    spacing * self._game.win_height,
                )
            )
            self._game.window.blit(word_surface, word_rect)
            if index != len(text) - 2:
                spacing += 0.1
            else:
                spacing += 0.25
        pygame.display.flip()

    def draw(self):
        """
        Draw the view based on current changes in the model.
        """
        self._game.window.fill((255, 255, 255))
        self._game._ground.draw_ground()
        self._game._player.draw_player(self._game._ground)
        for cactus in self._game._cacti:
            cactus.draw()
        for ptero in self._game._pterodactyls:
            ptero.draw_ptero()
        if self._game._score >= 0:
            score_text = self._FONT.render(
                f"{math.floor(self._game._score):05d}", True, (0, 0, 0)
            )
            score_rect = score_text.get_rect(
                topright=(self._game.win_width - 10, 10)
            )
            self._game.window.blit(score_text, score_rect)
        else:
            calibration_text = self._FONT.render(
                "Calibrating...", True, (0, 0, 0)
            )
            calibration_rect = calibration_text.get_rect(
                midtop=(self._game.win_width / 2, self._game.win_height / 2)
            )
            self._game.window.blit(calibration_text, calibration_rect)

    def show_end_screen(self):
        # Draw game over message
        game_over_text = pygame.image.load(
            "images/game-over.jpg"
        ).convert_alpha()
        game_over_rect = game_over_text.get_rect(
            center=(
                self._game.win_width // 2,
                self._game.win_height // 2 - 50,
            )
        )
        self._game.window.blit(game_over_text, game_over_rect)
        # Draw restart button
        pygame.draw.rect(
            self._game.window, (0, 0, 255), self._game._restart_button
        )
        restart_text = pygame.image.load(
            "images/restart-button.jpg"
        ).convert_alpha()
        restart_rect = restart_text.get_rect(
            center=self._game._restart_button.center
        )
        self._game.window.blit(restart_text, restart_rect)
        pygame.display.flip()
