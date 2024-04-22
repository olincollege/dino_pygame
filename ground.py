import pygame


class Ground:
    def __init__(self, winwidth, winheight, surface, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.winwidth = winwidth
        self.winheight = winheight
        self._surface = surface

        self.rect.y = self.winheight - self.rect.height

        self.x1 = 0
        self.x2 = self.rect.width
        self.speed = 5

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 + self.rect.width < 0:
            self.x1 = self.x2 + self.rect.width
        if self.x2 + self.rect.width < 0:
            self.x2 = self.x1 + self.rect.width

    def draw_ground(self):
        self._surface.blit(self.image, (self.x1, self.rect.y))
        self._surface.blit(self.image, (self.x2, self.rect.y))

    def get_rect(self):
        return pygame.Rect(0, self.rect.y, self.winwidth, 0.1 * self.winheight)
