# food.py

import pygame
import random
from config import BLOCK_SIZE, RED

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_size = BLOCK_SIZE
        self.x, self.y = self.generate_food_position()

    def draw(self, window):
        pygame.draw.rect(window, RED, [self.x, self.y, self.block_size, self.block_size])

    def generate_food_position(self):
        x = round(random.randrange(0, self.width - self.block_size) / self.block_size) * self.block_size
        y = round(random.randrange(0, self.height - self.block_size) / self.block_size) * self.block_size
        return x, y
