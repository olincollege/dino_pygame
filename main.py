"""
Dino Game

This program implements a simple Dino Game using Pygame.

Classes:
    Player: Represents the player character in the game.
    Ground: Represents the ground in the game.
    Cactus: Represents the obstacles (cacti) in the game.
"""

import random
import math
import pygame
from player import Player
from ground import Ground
from cactus import Cactus
from pterodactyl import Pterodactyl

pygame.init()  # pylint: disable=no-member

WIN_WIDTH = 791
WIN_HEIGHT = 201

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Dino Game")

player = Player(window, WIN_WIDTH, WIN_HEIGHT)
ground = Ground(WIN_WIDTH, WIN_HEIGHT, window, "images/ground.jpg")
cacti = pygame.sprite.Group()
pterodactyls = pygame.sprite.Group()

RUNNING = True

MIN_SPAWN_INTERVAL = 600  # Minimum interval in milliseconds
MAX_SPAWN_INTERVAL = 1800  # Maximum interval in milliseconds
spawn_interval = random.randint(MIN_SPAWN_INTERVAL, MAX_SPAWN_INTERVAL)

clock = pygame.time.Clock()
spawn_cactus_event = pygame.USEREVENT + 1  # pylint: disable=no-member
pygame.time.set_timer(spawn_cactus_event, 1500)

SPEED = 6
ACCELERATION = 0.001
MAX_SPEED = 13

SCORE = 500

# Font settings for displaying score
FONT_PATH = "PressStart2P-Regular.ttf"
FONT = pygame.font.Font(FONT_PATH, 16)

GAME_OVER = False
restart_button = pygame.Rect(WIN_WIDTH // 2 - 36, WIN_HEIGHT // 2 - 32, 72, 64)

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            RUNNING = False
        if not GAME_OVER:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:  # pylint: disable=no-member
                player.duck()
            else:
                player.unduck()
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                    player.jump(ground)
            if event.type == spawn_cactus_event:
                if SCORE < 500 or random.random() > 0.25:
                    new_cactus = Cactus(window, WIN_WIDTH, WIN_HEIGHT)
                    cacti.add(new_cactus)
                else:
                    ptero_heights = [
                        WIN_HEIGHT - 40,
                        WIN_HEIGHT - 60,
                        WIN_HEIGHT - 80,
                    ]
                    height = random.choice(ptero_heights)
                    new_ptero = Pterodactyl(
                        window, WIN_WIDTH, WIN_HEIGHT, height
                    )
                    pterodactyls.add(new_ptero)
        else:
            if (
                event.type
                == pygame.MOUSEBUTTONDOWN  # pylint: disable=no-member
            ):
                if restart_button.collidepoint(event.pos):
                    GAME_OVER = False
                    SCORE = 0
                    SPEED = 6
                    pterodactyls.empty()
                    cacti.empty()

    if not GAME_OVER:
        player.update(ground)
        ground.update(SPEED)
        cacti.update(SPEED)
        pterodactyls.update(SPEED)

        for cactus in cacti:
            offset_x = cactus.rect.left - player.rect.left
            offset_y = cactus.rect.top - player.rect.top

            if player.mask.overlap(cactus.mask, (offset_x, offset_y)):
                GAME_OVER = True

        for ptero in pterodactyls:
            offset_x = ptero.rect.left - player.rect.left
            offset_y = ptero.rect.top - player.rect.top

            if player.mask.overlap(ptero.mask, (offset_x, offset_y)):
                GAME_OVER = True

        if SPEED < MAX_SPEED:
            SPEED += ACCELERATION

        window.fill((255, 255, 255))
        ground.draw_ground()
        player.draw_player(ground)
        for cactus in cacti:
            cactus.draw()
        for ptero in pterodactyls:
            ptero.draw_ptero()

        SCORE += SPEED / 40

        score_text = FONT.render(f"{math.floor(SCORE):05d}", True, (0, 0, 0))
        score_rect = score_text.get_rect(topright=(WIN_WIDTH - 10, 10))
        window.blit(score_text, score_rect)

    if GAME_OVER:
        # Draw game over message
        game_over_text = pygame.image.load(
            "images/game-over.jpg"
        ).convert_alpha()
        game_over_rect = game_over_text.get_rect(
            center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 50)
        )
        window.blit(game_over_text, game_over_rect)

        # Draw restart button
        pygame.draw.rect(window, (0, 0, 255), restart_button)
        restart_text = pygame.image.load(
            "images/restart-button.jpg"
        ).convert_alpha()
        restart_rect = restart_text.get_rect(center=restart_button.center)
        window.blit(restart_text, restart_rect)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()  # pylint: disable=no-member
