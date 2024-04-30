"""
Model for Dino Game
"""

import random
import math
import pygame
from player import Player
from ground import Ground
from cactus import Cactus
from pterodactyl import Pterodactyl


class DinoGame:
    """
    Dino Game with basic play functionality

    Attributes:
        TBD!
    """

    _WIN_WIDTH = 791
    _WIN_HEIGHT = 201
    _MIN_SPAWN_INTERVAL = 600  # Minimum interval in milliseconds
    _MAX_SPAWN_INTERVAL = 1800  # Maximum interval in milliseconds
    _SPEED = 5.5
    _ACCELERATION = 0.001
    _MAX_SPEED = 13
    _score = -60
    _restart_button = pygame.Rect(
        _WIN_WIDTH // 2 - 36, _WIN_HEIGHT // 2 - 32, 72, 64
    )

    def __init__(self):
        """
        Initialize the dino game model.
        """
        self.window = pygame.display.set_mode(
            (self._WIN_WIDTH, self._WIN_HEIGHT)
        )
        self._player = Player(self.window, self._WIN_WIDTH, self._WIN_HEIGHT)
        self._ground = Ground(
            self._WIN_WIDTH, self._WIN_HEIGHT, self.window, "images/ground.jpg"
        )
        self._cacti = pygame.sprite.Group()
        self._pterodactyls = pygame.sprite.Group()
        self._spawn_interval = random.randint(
            self._MIN_SPAWN_INTERVAL, self._MAX_SPAWN_INTERVAL
        )
        self._clock = pygame.time.Clock()
        self._spawn_cactus_event = (
            pygame.USEREVENT + 1
        )  # pylint: disable=no-member
        pygame.time.set_timer(self._spawn_cactus_event, 1500)
        self._GAME_OVER = False
        self._running = True
        self._is_intro = True

    def restart(self):
        """
        Restart the game.
        """
        self._GAME_OVER = False
        self._score = -30
        self._SPEED = 6
        self._pterodactyls.empty()
        self._cacti.empty()
        self.update()

    def quit(self):
        """Quit out of the game"""
        self._running = False

    def start_game(self):
        """Exit the instructions stage"""
        self._is_intro = False

    @property
    def is_intro(self):
        """Get the _is_intro attribute"""
        return self._is_intro

    @property
    def ground(self):
        """Get the _ground attribute"""
        return self._ground

    @property
    def running(self):
        """Get the _running attribute"""
        return self._running

    @property
    def player(self):
        """Get the _player attribute"""
        return self._player

    @property
    def cacti(self):
        """Get the _cactiattribute"""
        return self._cacti

    @property
    def pterodactyls(self):
        """Get the _pterodactyls attribute"""
        return self._pterodactyls

    @property
    def score(self):
        """Get the _score attribute"""
        return self._score

    @property
    def win_width(self):
        """Get the _WIN_WIDTH attribute"""
        return self._WIN_WIDTH

    @property
    def win_height(self):
        """Get the _WIN_HEIGHT attribute"""
        return self._WIN_HEIGHT

    @property
    def game_over(self):
        """Get the _GAME_OVER attribute"""
        return self._GAME_OVER

    @property
    def restart_button(self):
        """Get the _restart_button attribute"""
        return self._restart_button

    def duck(self):
        self._player.duck()

    def unduck(self):
        self._player.unduck()

    def jump(self):
        self._player.jump()

    def update(self):
        self._player.update(self._ground)
        self._ground.update(self._SPEED)
        self._cacti.update(self._SPEED)
        self._pterodactyls.update(self._SPEED)
        for cactus in self._cacti:
            offset_x = cactus.rect.left - self._player.rect.left
            offset_y = cactus.rect.top - self._player.rect.top

            if self._player.mask.overlap(cactus.mask, (offset_x, offset_y)):
                self._GAME_OVER = True

        for ptero in self._pterodactyls:
            offset_x = ptero.rect.left - self._player.rect.left
            offset_y = ptero.rect.top - self._player.rect.top

            if self._player.mask.overlap(ptero.mask, (offset_x, offset_y)):
                self._GAME_OVER = True

        if self._SPEED < self._MAX_SPEED:
            self._SPEED += self._ACCELERATION
        self._score += self._SPEED / 40
        for event in pygame.event.get(pygame.USEREVENT + 1):
            if self._score >= 0:
                if self._score < 500 or random.random() > 0.25:
                    new_cactus = Cactus(
                        self.window, self._WIN_WIDTH, self._WIN_HEIGHT
                    )
                    self._cacti.add(new_cactus)
                    pass
                else:
                    ptero_heights = [
                        self._WIN_HEIGHT - 40,
                        self._WIN_HEIGHT - 60,
                        self._WIN_HEIGHT - 80,
                    ]
                    height = random.choice(ptero_heights)
                    new_ptero = Pterodactyl(
                        self.window, self._WIN_WIDTH, self._WIN_HEIGHT, height
                    )
                    self._pterodactyls.add(new_ptero)
        pygame.display.flip()
        self._clock.tick(60)
