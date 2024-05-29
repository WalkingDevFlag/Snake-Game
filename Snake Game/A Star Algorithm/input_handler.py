import pygame

def handle_input(event, snake):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and snake.x_change == 0:
            snake.x_change = -snake.block_size
            snake.y_change = 0
        elif event.key == pygame.K_RIGHT and snake.x_change == 0:
            snake.x_change = snake.block_size
            snake.y_change = 0
        elif event.key == pygame.K_UP and snake.y_change == 0:
            snake.y_change = -snake.block_size
            snake.x_change = 0
        elif event.key == pygame.K_DOWN and snake.y_change == 0:
            snake.y_change = snake.block_size
            snake.x_change = 0
