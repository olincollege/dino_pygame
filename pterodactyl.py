import pygame


class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, surface, winwidth, winheight, height):
        super().__init__()
        self.image = pygame.image.load("images/velociraptor-1.png")
        self.rect = self.image.get_rect()
        self._surface = surface
        self.winwidth = winwidth
        self.winheight = winheight

        self.rect.x = winwidth
        self.rect.y = height

        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):
        self.rect.x -= speed

        if self.rect.right < 0:
            self.kill()

    def draw(self):
        self._surface.blit(self.image, self.rect)
