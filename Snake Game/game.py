import pygame
from snake import Snake
from board import Board
from food import Food
from input_handler import handle_input
from collision_handler import check_collision
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, BLACK, RED, GRAY

class Game:
    def __init__(self):
        self.initialize()

    def initialize(self):
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        # Game settings
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 35)

        # Initialize snake and board
        self.snake = Snake(self.width, self.height, BLOCK_SIZE)
        self.board = Board(self.width, self.height, BLOCK_SIZE)
        self.food = Food(self.width, self.height)

    def run(self):
        game_over = False
        game_close = False

        while not game_over:
            while game_close:
                self.window.fill(BLACK)
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
                handle_input(event, self.snake)

            self.snake.update()

            # Check for collisions
            if check_collision(self.snake, self.width, self.height):
                game_close = True

            # Check if snake eats food
            if self.snake.head_position() == (self.food.x, self.food.y):
                self.food.x, self.food.y = self.food.generate_food_position()
                self.snake.grow()

            # Draw the game
            self.window.fill(BLACK)
            self.board.draw_grid(self.window)
            self.food.draw(self.window)
            self.snake.draw(self.window)
            pygame.display.update()

            # Control the game speed
            self.clock.tick(15)

        pygame.quit()
        quit()

    def show_game_over_message(self):
        game_over_text = self.font.render("Game Over! Press R to Restart", True, RED)
        self.window.blit(game_over_text, [self.width / 6, self.height / 3])
