import pygame
import math


class Player(pygame.sprite.Sprite):

    def __init__(self, surface, win_width, win_height) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = [
            pygame.image.load("images/dino-run-1.png"),
            pygame.image.load("images/dino-run-2.png"),
            pygame.image.load("images/dino-run-3.png"),
        ]
        self.rect = self.image[0].get_rect()
        self.speed = [0, 1]
        self._surface = surface
        self.win_height = win_height
        self.win_width = win_width
        self.animation_frame = 0

    def draw_player(self, ground):
        if self.animation_frame > len(self.image) - 0.2:
            self.animation_frame = 0
        else:
            self.animation_frame += 0.2
        if self.rect.bottom < ground.get_rect().top + ground.get_rect().height / 2:
            self._surface.blit(self.image[0], self.rect)
        else:
            self._surface.blit(self.image[math.floor(self.animation_frame)], self.rect)

    def update(self, ground):
        self.rect = self.rect.move(self.speed)
        if self.rect.bottom > ground.get_rect().top + ground.get_rect().height / 2:
            self.speed[1] -= self.speed[1]
        else:
            self.speed[1] += 0.4

    def jump(self, ground):
        if self.rect.bottom >= ground.get_rect().top:
            self.speed[1] -= 8
