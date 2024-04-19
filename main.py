# import pygame package
import pygame
import player

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
window = pygame.display.set_mode((500, 500))

# creating a bool value which checks
# if game is running
RUNNING = True

# setting variable to storecolor
COLOR = "white"
P_COLOR = "red"

x_position = 100
y_position = 100
height = 50
width = 50

p = player.Player(x_position, y_position, height, width, window, P_COLOR)

# keep game running till running is true
while RUNNING:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    # set background color to our window
    window.fill(COLOR)

    # Update our window
    pygame.display.flip()
    p.draw_player()
    # if color is red change it to green and
    # vice-versa
