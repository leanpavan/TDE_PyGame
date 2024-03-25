import os
import pygame
from sys import exit

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

# SCREEN DATA
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CENTER = 400, 300

# Circle
circle = pygame.image.load(os.path.join("data", "circle.png"))
circle = pygame.transform.scale(circle, (128, 128))
circlerect = circle.get_rect()
circlerect.center = (SCREEN_CENTER)

#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Moving Image")

clock = pygame.time.Clock()
running = True
delta_time = 0

# PLAYER
player_x = 400
player_y = 300
speed = 10
right_key = pygame.K_d
left_key =pygame.K_a
up_key = pygame.K_w
down_key = pygame.K_s

while True:
    #fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")
    screen.blit(circle, (player_x, player_y))
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    player_x += (keys[right_key] - keys[left_key]) * speed
    player_y += (keys[down_key] - keys[up_key]) * speed


    delta_time = clock.tick(60) / 1000
    #poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

pygame.quit()