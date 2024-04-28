# import pygame package
import pygame
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

SPEED = 6
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
    ground.update(SPEED)
    cacti.update(SPEED)

    for cactus in cacti:
        offset_x = cactus.rect.left - player.rect.left
        offset_y = cactus.rect.top - player.rect.top

        if player.mask.overlap(cactus.mask, (offset_x, offset_y)):
            RUNNING = False

    if SPEED < MAX_SPEED:
        SPEED += ACCELERATION

    window.fill((255, 255, 255))
    ground.draw_ground()
    player.draw_player(ground)
    cacti.draw(window)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()  # pylint: disable=no-member
