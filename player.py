"""Module defining the Player class.

The Player class represents the player character in the game. It handles the
player's movement, animation, jumping, and ducking behavior.

Classes:
    Player: Represents the player character in the game.
"""

import math
import pygame


class Player(
    pygame.sprite.Sprite
):  # pylint: disable=too-many-instance-attributes
    """A class representing the player character in the game."""

    def __init__(self, surface, win_width, win_height) -> None:
        """Initialize the Player object.

        Args:
            surface (pygame.Surface): The surface on which the player will be
            drawn.
            win_width (int): The width of the game window.
            win_height (int): The height of the game window.
        """
        super().__init__()
        self._image = [
            pygame.image.load("images/dino-run-1.png").convert_alpha(),
            pygame.image.load("images/dino-run-2.png").convert_alpha(),
            pygame.image.load("images/dino-run-3.png").convert_alpha(),
        ]
        self.rect = self._image[0].get_rect()
        self.speed = [0, 1]
        self._surface = surface
        self._win_height = win_height
        self._win_width = win_width
        self._animation_frame = 0
        self.mask = 0

        self.is_ducking = False
        self._ducking_images = [
            pygame.image.load("images/dino-duck-1.png").convert_alpha(),
            pygame.image.load("images/dino-duck-2.png").convert_alpha(),
        ]

    def draw_player(self, ground):
        """Draw the player on the surface.

        Args:
            ground (Ground): The ground object used to determine the player's
            position.
        """
        if self.is_ducking:
            if self._animation_frame > len(self._ducking_images) - 0.2:
                self._animation_frame = 0
            else:
                self._animation_frame += 0.2
            self._surface.blit(
                self._ducking_images[math.floor(self._animation_frame)],
                self.rect,
            )
            self.mask = pygame.mask.from_surface(
                self._ducking_images[math.floor(self._animation_frame)]
            )
        else:
            if self._animation_frame > len(self._image) - 0.2:
                self._animation_frame = 0
            else:
                self._animation_frame += 0.2
            if (
                self.rect.bottom
                < ground.get_rect().top + ground.get_rect().height / 2
            ):
                self._surface.blit(self._image[0], self.rect)
                self.mask = pygame.mask.from_surface(self._image[0])
            else:
                self._surface.blit(
                    self._image[math.floor(self._animation_frame)], self.rect
                )
                self.mask = pygame.mask.from_surface(
                    self._image[math.floor(self._animation_frame)]
                )

    def update(self, ground):
        """Update the player's position and animation frame.

        Args:
            ground (Ground): The ground object used to determine the player's
            position.
        """
        self.rect = self.rect.move(self.speed)
        if (
            self.rect.bottom
            > ground.get_rect().top + ground.get_rect().height / 2
        ):
            self.speed[1] -= self.speed[1]
        else:
            self.speed[1] += 0.5

        if self.is_ducking:
            self.rect = self._ducking_images[0].get_rect(
                bottomleft=self.rect.bottomleft
            )
        else:
            self.rect = self._image[0].get_rect(bottomleft=self.rect.bottomleft)

    def jump(self, ground):
        """Make the player character jump.

        Args:
            ground (Ground): The ground object used to determine if the player
            can jump.
        """
        if self.rect.bottom >= ground.get_rect().top:
            self.speed[1] -= 8

    def duck(self):
        """Make the player character duck."""
        self.is_ducking = True

    def unduck(self):
        """Make the player character stop ducking."""
        self.is_ducking = False
