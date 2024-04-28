import pygame
import random


class Cactus(pygame.sprite.Sprite):
    def __init__(self, surface, image_path, winwidth, winheight):
        super(Cactus, self).__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self._surface = surface
        self.winwidth = winwidth
        self.winheight = winheight

        self.rect.x = winwidth
        self.rect.y = winheight - self.rect.height

        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):
        self.rect.x -= speed
        print(speed)

        if self.rect.right < 0:
            self.kill()

    def draw(self):
        self._surface.blit(self.image, self.rect)
