import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (50, 50, 50)

# Game settings
block_size = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Initialize high score
high_score = 0

# Game over message
def game_over_message():
    msg = font.render("Game Over! Press R to Restart", True, red)
    win.blit(msg, [width / 6, height / 3])

# Draw grid
def draw_grid():
    for x in range(0, width, block_size):
        pygame.draw.line(win, gray, (x, 0), (x, height))
    for y in range(0, height, block_size):
        pygame.draw.line(win, gray, (0, y), (width, y))

# Main game loop
def game_loop():
    global high_score
    
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    # Initial food spawn
    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            win.fill(black)
            game_over_message()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        if score > high_score:
                            high_score = score
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        win.fill(black)

        draw_grid()

        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])
        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake:
            pygame.draw.rect(win, white, [segment[0], segment[1], block_size, block_size])

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1

        pygame.display.update()

        clock.tick(15)

    pygame.quit()
    quit()

game_loop()
