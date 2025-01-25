import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 20
BG_COLOR = (25, 25, 25)
SNAKE_COLOR = (0, 255, 127)
FOOD_COLOR = (255, 50, 50)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 150, 200)

# Initialize screen and settings
default_settings = {
    'width': 800,
    'height': 600,
    'fps': 15
}

screen = pygame.display.set_mode((default_settings['width'], default_settings['height']))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Fonts
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 36)

class Snake:
    def __init__(self, width, height):
        self.body = [(width//2, height//2)]
        self.direction = (0, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def check_collision(self):
        return self.body[0] in self.body[1:]

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        x = random.randrange(0, self.width, GRID_SIZE)
        y = random.randrange(0, self.height, GRID_SIZE)
        self.position = (x, y)

def draw_snake(snake):
    for i, (x, y) in enumerate(snake.body):
        radius = GRID_SIZE // 2 - 2
        if i == 0:
            pygame.draw.circle(screen, SNAKE_COLOR, (x + GRID_SIZE//2, y + GRID_SIZE//2), radius)
        else:
            pygame.draw.rect(screen, SNAKE_COLOR, (x, y, GRID_SIZE-2, GRID_SIZE-2), border_radius=4)

def draw_food(food):
    x, y = food.position
    pygame.draw.circle(screen, FOOD_COLOR, (x + GRID_SIZE//2, y + GRID_SIZE//2), GRID_SIZE//2 - 2)

def draw_button(text, rect, hover):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=5)
    text_surf = font_small.render(text, True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def draw_grid(width, height):
    grid_color = (50, 50, 50, 25)  
    for x in range(0, width, GRID_SIZE):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height))
    for y in range(0, height, GRID_SIZE):
        pygame.draw.line(screen, grid_color, (0, y), (width, y))

def game_loop(settings):
    snake = Snake(settings['width'], settings['height'])
    food = Food(settings['width'], settings['height'])
    score = 0
    running = True
    game_over = False

    while running:
        screen.fill(BG_COLOR)
        draw_grid(settings['width'], settings['height'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        return
                else:
                    if event.key == pygame.K_UP and snake.direction != (0, 1):
                        snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                        snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                        snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                        snake.direction = (1, 0)

        if not game_over:
            snake.move()
            head_x, head_y = snake.body[0]

            # Collision checks
            if (head_x < 0 or head_x >= settings['width'] or 
                head_y < 0 or head_y >= settings['height'] or 
                snake.check_collision()):
                game_over = True

            # Food handling
            if snake.body[0] == food.position:
                snake.grow = True
                score += 1
                food.spawn()

            draw_snake(snake)
            draw_food(food)

            score_text = font_small.render(f"Score: {score}", True, TEXT_COLOR)
            screen.blit(score_text, (10, 10))
        else:
            game_over_text = font_large.render("Game Over!", True, TEXT_COLOR)
            screen.blit(game_over_text, (settings['width']//2 - game_over_text.get_width()//2, settings['height']//3))

            final_score_text = font_medium.render(f"Final Score: {score}", True, TEXT_COLOR)
            screen.blit(final_score_text, (settings['width']//2 - final_score_text.get_width()//2, settings['height']//2))

            mouse_pos = pygame.mouse.get_pos()
            restart_rect = pygame.Rect(settings['width']//2 - 100, settings['height']*2//3, 200, 40)
            hover_restart = restart_rect.collidepoint(mouse_pos)
            draw_button("Restart (SPACE)", restart_rect, hover_restart)

            quit_rect = pygame.Rect(settings['width']//2 - 100, settings['height']*2//3 + 60, 200, 40)
            hover_quit = quit_rect.collidepoint(mouse_pos)
            draw_button("Quit", quit_rect, hover_quit)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_restart:
                    return
                elif hover_quit:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(settings['fps'])

def settings_menu(settings):
    global screen
    while True:
        screen.fill(BG_COLOR)
        title_text = font_large.render("Settings", True, TEXT_COLOR)
        title_y = settings['height'] // 8
        screen.blit(title_text, (settings['width']//2 - title_text.get_width()//2, title_y))

        # Vertical center calculation
        panel_start_y = title_y + title_text.get_height() + 50
        available_height = settings['height'] - panel_start_y - 100
        center_y = panel_start_y + available_height // 2

        # Common dimensions
        button_width = 220
        button_height = 40
        vertical_spacing = 20

        # Left Panel: Resolution
        res_text = font_medium.render("Resolution", True, TEXT_COLOR)
        resolutions = [
            (800, 600),
            (1024, 768),
            (1280, 720)
        ]
        
        content_height = res_text.get_height() + len(resolutions)*(button_height + vertical_spacing)
        panel_y = center_y - content_height//2

        screen.blit(res_text, (settings['width']//4 - res_text.get_width()//2, panel_y))
        
        res_buttons = []
        for i, res in enumerate(resolutions):
            rect = pygame.Rect(
                settings['width']//4 - button_width//2,
                panel_y + res_text.get_height() + 30 + i*(button_height + vertical_spacing),
                button_width,
                button_height
            )
            res_buttons.append((res, rect))
            hover = rect.collidepoint(pygame.mouse.get_pos())
            text = f"{res[0]}x{res[1]}" + (" ✓" if (res[0], res[1]) == (settings['width'], settings['height']) else "")
            draw_button(text, rect, hover)

        # Right Panel: Speed
        speed_text = font_medium.render("Speed", True, TEXT_COLOR)
        speeds = [("Slow", 10), ("Medium", 15), ("Fast", 20)]
        
        content_height = speed_text.get_height() + len(speeds)*(button_height + vertical_spacing)
        panel_y = center_y - content_height//2

        screen.blit(speed_text, (3*settings['width']//4 - speed_text.get_width()//2, panel_y))
        
        speed_buttons = []
        for i, (name, fps) in enumerate(speeds):
            rect = pygame.Rect(
                3*settings['width']//4 - button_width//2,
                panel_y + speed_text.get_height() + 30 + i*(button_height + vertical_spacing),
                button_width,
                button_height
            )
            speed_buttons.append((fps, rect))
            hover = rect.collidepoint(pygame.mouse.get_pos())
            text = name + (" ✓" if fps == settings['fps'] else "")
            draw_button(text, rect, hover)

        # Back Button
        back_rect = pygame.Rect(
            settings['width']//2 - button_width//2,
            settings['height'] - 100,
            button_width,
            button_height
        )
        hover_back = back_rect.collidepoint(pygame.mouse.get_pos())
        draw_button("Back", back_rect, hover_back)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for res, rect in res_buttons:
                    if rect.collidepoint(mouse_pos):
                        settings.update({'width': res[0], 'height': res[1]})
                        screen = pygame.display.set_mode((res[0], res[1]))
                for fps, rect in speed_buttons:
                    if rect.collidepoint(mouse_pos):
                        settings['fps'] = fps
                if back_rect.collidepoint(mouse_pos):
                    return

        pygame.display.flip()
        clock.tick(settings['fps'])

def main_menu(settings):
    while True:
        screen.fill(BG_COLOR)
        title_text = font_large.render("SNAKE GAME", True, TEXT_COLOR)
        screen.blit(title_text, (settings['width']//2 - title_text.get_width()//2, settings['height']//4))

        mouse_pos = pygame.mouse.get_pos()

        # Start button
        start_rect = pygame.Rect(settings['width']//2 - 100, settings['height']//2, 200, 40)
        hover_start = start_rect.collidepoint(mouse_pos)
        draw_button("Start Game", start_rect, hover_start)

        # Settings button
        settings_rect = pygame.Rect(settings['width']//2 - 100, settings['height']//2 + 60, 200, 40)
        hover_settings = settings_rect.collidepoint(mouse_pos)
        draw_button("Settings", settings_rect, hover_settings)

        # Quit button
        quit_rect = pygame.Rect(settings['width']//2 - 100, settings['height']//2 + 120, 200, 40)
        hover_quit = quit_rect.collidepoint(mouse_pos)
        draw_button("Quit", quit_rect, hover_quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_start:
                    game_loop(settings)
                elif hover_settings:
                    settings_menu(settings)
                elif hover_quit:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(settings['fps'])

if __name__ == "__main__":
    settings = default_settings.copy()
    main_menu(settings)