"""
View for dino game
"""

import pygame
import math


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

        score_text = self._FONT.render(
            f"{math.floor(self._game._score):05d}", True, (0, 0, 0)
        )
        score_rect = score_text.get_rect(
            topright=(self._game.win_width - 10, 10)
        )
        self._game.window.blit(score_text, score_rect)

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
