import pygame
from config import Config

class Board:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.colors = Config().colors

    def draw_grid(self, window):
        for x in range(0, self.width, self.block_size):
            pygame.draw.line(window, self.colors['gray'], (x, 0), (x, self.height))
        for y in range(0, self.height, self.block_size):
            pygame.draw.line(window, self.colors['gray'], (0, y), (self.width, y))

    def draw_background(self, window):
        window.fill(self.colors['black'])
