# entities.py
import random
from config import GRID_SIZE

class Snake:
    def __init__(self, width, height):
        self.body = [(width//2, height//2)]
        self.body_set = set(self.body)
        self.direction = (0, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
        
        self.body.insert(0, new_head)
        self.body_set.add(new_head)
        
        if not self.grow:
            tail = self.body.pop()
            self.body_set.discard(tail)
        else:
            self.grow = False

        return new_head in self.body_set - {new_head}

class Food:
    def __init__(self, width, height, snake):
        self.width = width
        self.height = height
        self.snake = snake
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        while True:
            x = random.randrange(0, self.width, GRID_SIZE)
            y = random.randrange(0, self.height, GRID_SIZE)
            self.position = (x, y)
            if self.position not in self.snake.body_set:
                break