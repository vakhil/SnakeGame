import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Manually Creating Rect Objects")

# Create Rect objects manually
rect1 = pygame.Rect(100, 100, 50, 50)  # (x, y, width, height)
rect2 = pygame.Rect(200, 200, 70, 30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the Rect objects
    pygame.draw.rect(screen, (255, 0, 0), rect1)  # Red rectangle
    pygame.draw.rect(screen, (0, 0, 255), rect2)  # Blue rectangle

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
