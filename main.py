import os
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

circle = pygame.image.load(os.path.join("data", "circle.png"))
circlerect = circle.get_rect()

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
delta_time = 0

player_pos = pygame.Vector2(screen.get_width())

while running:
    #poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(circle, circlerect)
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000

pygame.quit()