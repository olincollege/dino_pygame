"""Module defining the Cactus class.

The Cactus class represents the player character in the game. It handles the 
cactus's movement behavior.

Classes:
    Cactus: Represents the cactus character in the game.
"""

import random
import pygame


class Cactus(pygame.sprite.Sprite):
    """A class representing a cactus obstacle in the game."""

    def __init__(self, surface, image_paths, winwidth, winheight):
        """Initialize the Cactus object.

        Args:
            surface (pygame.Surface): The surface on which the cactus will be
            drawn.
            image_path (str): The file path to the image of the cactus.
            winwidth (int): The width of the game window.
            winheight (int): The height of the game window.
        """
        super().__init__()
        self.image = pygame.image.load(random.choice(image_paths)).convert_alpha()
        self.rect = self.image.get_rect()
        self._surface = surface
        self.winwidth = winwidth
        self.winheight = winheight

        self.rect.x = winwidth
        self.rect.y = winheight - self.rect.height

        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):
        """Update the position of the cactus.

        Args:
            speed (int): The speed at which the cactus moves horizontally.
        """
        self.rect.x -= speed

        if self.rect.right < 0:
            self.kill()

    def draw(self):
        """Draw the cactus on the surface."""
        self._surface.blit(self.image, self.rect)
