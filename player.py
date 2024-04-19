import pygame


class Player:
    def __init__(self, posx, posy, height, width, surface, color) -> None:
        self.velocity = 0
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        self._surface = surface
        self.color = color

    def draw_player(self):
        pygame.draw.rect(
            self._surface,
            self.color,
            pygame.Rect(self.posx, self.posy, self.width, self.height),
        )
