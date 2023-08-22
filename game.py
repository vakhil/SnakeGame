import pygame
import sys


pygame.init()

class Snake :
     def __init__(self) -> None:
         self.body_cells = []


# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Example")


# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load background asset
background_asset = pygame.Surface((10, 10))
background_asset.fill(WHITE)

# Create grid of background assets
grid_size = 10  # 10x10 grid
grid_spacing = 10
grid = [[background_asset.get_rect(topleft=(x, y)) for x in range(0, screen_width, grid_spacing)] for y in range(0, screen_height, grid_spacing)]


# Game loop
selected_cell = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for row in grid:
                for cell in row:
                    if cell.collidepoint(event.pos):
                        selected_cell = cell

    # Clear the screen
    screen.fill(BLACK)


    # Draw the grid
    for row in grid:
        for cell in row:
            pygame.draw.rect(screen, WHITE, cell)

    

    # Color the selected cell
    if selected_cell:    # for row in grid:
        pygame.draw.rect(screen, RED, selected_cell)
           

    # Update the display
    pygame.display.flip()

#Clean up
pygame.quit()
sys.exit()