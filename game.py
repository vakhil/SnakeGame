import pygame
import sys


pygame.init()



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


class Snake :

    def __init__(self) -> None:
         self.body_cells = []

    def __init__(self, snake_head_x, snake_head_y,screen) :
        self.snake_length = 5
        self.screen = screen
        self.snake_size = 10

        self.body_cells = []
        for i in range(0,self.snake_length) :
            self.body_cells.append(pygame.Rect((snake_head_x - (i+1)*self.snake_size,snake_head_y),(self.snake_size,self.snake_size)))

    def draw_snake_on_screen(self):
        index = 0
        # This is the snake head. Color it with RED
        for body_part in self.body_cells:
            if index == 0 :
                pygame.draw.rect(self.screen,RED,body_part)
                index += 1
            else :
                pygame.draw.rect(self.screen,BLACK,body_part)

    def generate_snake_body(self, snake_head_x,snake_head_y):
        index = 0
        self.body_cells = []
        for i in range(0,self.snake_length) :
            self.body_cells.append(pygame.Rect((snake_head_x - (i+1)*self.snake_size,snake_head_y),(self.snake_size,self.snake_size)))


    def update_snake_position(self):
        index = 0
        head = self.body_cells[0]
        print(head.topleft[0] +10)
        self.generate_snake_body(head.topleft[0] +10,head.topleft[1]+10)


    def get_snake_body(self):
        return self.body_cells



# Game loop
selected_cell = None
running = True
snake = None
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

    #Draw the snake if a click has been made on the screen 
    if snake :
        print("The snake has been created")
        # snake.update_snake_position()
        snake.draw_snake_on_screen()
        



    # Draw the grid
    for row in grid:
        for cell in row:
            pygame.draw.rect(screen, WHITE, cell)
            

    

    # Color the selected cell
    # if selected_cell:    # for row in grid:
    #     pygame.draw.rect(screen, RED, selected_cell)
           
    #Draw Snake Body
    if selected_cell:
        snake = Snake(selected_cell.topleft[0],selected_cell.topleft[1],screen)
        # snake.drawOnScreen()
        # for bodyParts in snake.get_snake_body() :
        #     pygame.draw.rect(screen,BLACK,bodyParts)

    # Update the display
    pygame.display.flip()

#Clean up
pygame.quit()
sys.exit()