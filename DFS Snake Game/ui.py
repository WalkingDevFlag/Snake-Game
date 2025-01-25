import pygame
from config import *


def draw_laser_path(screen, path):
    if not path:
        return
    
    # Create glowing effect with multiple lines
    for i in range(3):
        alpha = 100 - i*30
        width = 3 - i
        for j in range(len(path)-1):
            start = (path[j][0] + GRID_SIZE//2, path[j][1] + GRID_SIZE//2)
            end = (path[j+1][0] + GRID_SIZE//2, path[j+1][1] + GRID_SIZE//2)
            pygame.draw.line(
                screen, 
                (255, 50, 50, alpha),  # Red with transparency
                start,
                end,
                width
            )
    
    # Draw main solid line
    for j in range(len(path)-1):
        start = (path[j][0] + GRID_SIZE//2, path[j][1] + GRID_SIZE//2)
        end = (path[j+1][0] + GRID_SIZE//2, path[j+1][1] + GRID_SIZE//2)
        pygame.draw.line(
            screen, 
            (255, 0, 0),  # Solid red
            start,
            end,
            2
        )


def draw_snake(screen, snake):
    for i, (x, y) in enumerate(snake.body):
        radius = GRID_SIZE // 2 - 2
        if i == 0:
            pygame.draw.circle(screen, SNAKE_COLOR, (x + GRID_SIZE//2, y + GRID_SIZE//2), radius)
        else:
            pygame.draw.rect(screen, SNAKE_COLOR, (x, y, GRID_SIZE-2, GRID_SIZE-2), border_radius=4)

def draw_food(screen, food):
    x, y = food.position
    pygame.draw.circle(screen, FOOD_COLOR, (x + GRID_SIZE//2, y + GRID_SIZE//2), GRID_SIZE//2 - 2)

def draw_button(screen, text, rect, hover, font):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=5)
    text_surf = font.render(text, True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def draw_grid(width, height):
    grid_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    grid_color = (50, 50, 50, 25)
    for x in range(0, width, GRID_SIZE):
        pygame.draw.line(grid_surface, grid_color, (x, 0), (x, height))
    for y in range(0, height, GRID_SIZE):
        pygame.draw.line(grid_surface, grid_color, (0, y), (width, y))
    return grid_surface

def get_fonts():
    return {
        'large': pygame.font.Font(None, 72),
        'medium': pygame.font.Font(None, 48),
        'small': pygame.font.Font(None, 36)
    }