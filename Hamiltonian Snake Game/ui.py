# ui.py
import pygame
from config import *

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