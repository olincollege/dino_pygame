# import pygame package
import pygame
import player
import ground
import time

# initializing imported module
pygame.init()  # pylint: disable=no-member

# displaying a window of height
# 500 and width 400
WIN_WIDTH = 791
WIN_HEIGHT = 201

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# creating a bool value which checks
# if game is running
RUNNING = True

# setting variable to storecolor
COLOR = "white"
P_COLOR = "red"
G_COLOR = "green"
GRAVITY = 0.1

X_POSITION = 100
Y_POSITION = 300
HEIGHT = 10
WIDTH = 10
DINO_IMG_PATH = "images/dino-run-1.png"
GROUND_IMG_PATH = "images/ground.jpg"


p = player.Player(window, WIN_WIDTH, WIN_HEIGHT)
g = ground.Ground(WIN_WIDTH, WIN_HEIGHT, window, GROUND_IMG_PATH)

# keep game running till running is true
while RUNNING:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            RUNNING = False
        if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
            if event.key == pygame.K_SPACE:  # pylint: disable=no-member
                p.jump(g)

    # set background color to our window
    window.fill(COLOR)
    # Update our window
    p.update(g)
    g.draw_ground()
    p.draw_player()

    pygame.display.flip()
    time.sleep(1 / 60)


pygame.quit()  # pylint: disable=no-member
# if color is red change it to green and
# vice-versa
