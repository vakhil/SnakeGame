import pygame
import sys


pygame.init()


# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Example")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False

    screen.fill((0,0,0))


    #Update the display 
    pygame.display.flip()

#Clean up
pygame.quit()
sys.exit()