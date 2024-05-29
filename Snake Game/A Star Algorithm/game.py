import pygame
from snake import Snake
from board import Board
from food import Food
from config import Config
from collision_handler import check_collision
from pathfinding import a_star_search

class Game:
    def __init__(self):
        self.initialize()

    def initialize(self):
        pygame.init()
        config = Config()
        self.width = config.screen_width
        self.height = config.screen_height
        self.block_size = config.block_size
        self.colors = config.colors

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 35)

        self.snake = Snake(self.width, self.height, self.block_size)
        self.board = Board(self.width, self.height, self.block_size)
        self.food = Food(self.width, self.height, self.block_size)

    def run(self):
        game_over = False
        game_close = False

        while not game_over:
            while game_close:
                self.board.draw_background(self.window)
                self.show_game_over_message()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_r:
                            self.initialize()
                            game_close = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            snake_body_set = set(tuple(segment) for segment in self.snake.body)
            start = (self.snake.x // self.block_size, self.snake.y // self.block_size)
            goal = (self.food.x // self.block_size, self.food.y // self.block_size)
            path = a_star_search(start, goal, self.create_grid(), snake_body_set)

            if path:
                next_move = path[0]
                print("Next move:", next_move)  # Debug print
                self.snake.x_change = (next_move[0] * self.block_size) - self.snake.x
                self.snake.y_change = (next_move[1] * self.block_size) - self.snake.y
                self.snake.update()
            else:
                print("No path found, not moving")

            if check_collision(self.snake, self.width, self.height):
                game_close = True

            if self.snake.head_position() == (self.food.x, self.food.y):
                self.food.x, self.food.y = self.food.generate_food_position()
                self.snake.grow()
                print("Ate apple, new food at:", (self.food.x, self.food.y))  # Debug print
                path = a_star_search(start, goal, self.create_grid(), snake_body_set)

            self.board.draw_background(self.window)
            self.board.draw_grid(self.window)
            self.food.draw(self.window)
            self.snake.draw(self.window)
            self.draw_path(path)
            pygame.display.update()

            self.clock.tick(15)

        pygame.quit()
        quit()

    def create_grid(self):
        grid = [[0 for _ in range(self.width // self.block_size)] for _ in range(self.height // self.block_size)]
        return grid

    def show_game_over_message(self):
        game_over_text = self.font.render("Game Over! Press R to Restart", True, self.colors['red'])
        self.window.blit(game_over_text, [self.width / 6, self.height / 3])

    def draw_path(self, path):
        if path:
            path_color = self.colors['translucent_red']
            for i in range(len(path) - 1):
                start = (path[i][0] * self.block_size + self.block_size // 2, path[i][1] * self.block_size + self.block_size // 2)
                end = (path[i + 1][0] * self.block_size + self.block_size // 2, path[i + 1][1] * self.block_size + self.block_size // 2)
                pygame.draw.line(self.window, path_color, start, end, 3)
