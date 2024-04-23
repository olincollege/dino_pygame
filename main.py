# import pygame package
import pygame
import time
from player import Player
from ground import Ground
from cactus import Cactus

pygame.init()  # pylint: disable=no-member

WIN_WIDTH = 791
WIN_HEIGHT = 201
CACTUS_IMG_PATH = "images/cactus-group.png"

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Dino Game")

player = Player(window, WIN_WIDTH, WIN_HEIGHT)
ground = Ground(WIN_WIDTH, WIN_HEIGHT, window, "images/ground.jpg")
cacti = pygame.sprite.Group()

RUNNING = True
clock = pygame.time.Clock()
spawn_cactus_event = pygame.USEREVENT + 1  # pylint: disable=no-member
pygame.time.set_timer(spawn_cactus_event, 1500)

speed = 6
ACCELERATION = 0.001
MAX_SPEED = 13


while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            RUNNING = False
        if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
            if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                player.jump(ground)
        if event.type == spawn_cactus_event:
            new_cactus = Cactus(window, CACTUS_IMG_PATH, WIN_WIDTH, WIN_HEIGHT)
            cacti.add(new_cactus)

    player.update(ground)
    ground.update(speed)
    cacti.update(speed)

    collisions = pygame.sprite.spritecollide(player, cacti, False)
    if collisions:
        RUNNING = False

    if speed < MAX_SPEED:
        speed += ACCELERATION

    window.fill((255, 255, 255))
    ground.draw_ground()
    player.draw_player(ground)
    cacti.draw(window)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()  # pylint: disable=no-member
