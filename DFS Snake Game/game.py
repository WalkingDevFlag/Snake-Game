import pygame
import sys
from entities import Snake, Food
from pathfinding import DFSPathfinder
from ui import draw_snake, draw_food, draw_button, draw_grid, draw_laser_path, get_fonts
from config import *

def game_loop(settings):
    screen = settings['screen']
    fonts = get_fonts()
    clock = pygame.time.Clock()
    grid_surface = draw_grid(settings['width'], settings['height'])
    
    pathfinder = DFSPathfinder(settings['width'], settings['height'], GRID_SIZE)
    snake = Snake(settings['width'], settings['height'])
    food = Food(settings['width'], settings['height'], snake)
    
    current_path = []
    score = 0
    running = True
    game_over = False
    victory = False
    show_speed_options = False
    base_fps = 15
    current_speed = 0
    total_cells = (settings['width'] // GRID_SIZE) * (settings['height'] // GRID_SIZE)
    max_score = total_cells - 1
    path_lock = False
    last_direction = (0, 0)

    while running:
        screen.fill(BG_COLOR)
        screen.blit(grid_surface, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over and 'speed_button_rect' in locals() and speed_button_rect.collidepoint(mouse_pos):
                    show_speed_options = not show_speed_options
                elif show_speed_options:
                    for i, _ in enumerate(speed_options):
                        option_rect = pygame.Rect(
                            speed_button_rect.x,
                            speed_button_rect.y + (i+1)*45,
                            speed_button_rect.width,
                            speed_button_rect.height
                        )
                        if option_rect.collidepoint(mouse_pos):
                            current_speed = i
                            show_speed_options = False
                if game_over:
                    if 'restart_rect' in locals() and restart_rect.collidepoint(mouse_pos):
                        game_loop(settings)
                        return
                    elif 'quit_rect' in locals() and quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        if not game_over:
            moves = speed_options[current_speed]["moves"]
            for _ in range(moves):
                if not path_lock or not current_path:
                    current_path = pathfinder.find_path(
                        snake.body[0], 
                        food.position,
                        snake.body_set
                    )
                    path_lock = True

                if not current_path or len(current_path) < 2:
                    game_over = True
                    break
                
                next_node = current_path[1]
                dx = (next_node[0] - snake.body[0][0]) // GRID_SIZE
                dy = (next_node[1] - snake.body[0][1]) // GRID_SIZE

                # Prevent reverse direction
                if (dx, dy) == (-last_direction[0], -last_direction[1]):
                    current_path = []
                    path_lock = False
                    continue

                last_direction = (dx, dy)
                snake.direction = (dx, dy)
                collision = snake.move()

                # Update path
                if len(current_path) > 1:
                    current_path.pop(0)
                else:
                    path_lock = False

                # Collision detection
                head = snake.body[0]
                boundary_collision = (
                    head[0] < 0 or head[0] >= settings['width'] or
                    head[1] < 0 or head[1] >= settings['height']
                )
                game_over = boundary_collision or collision

                # Food handling
                if head == food.position:
                    snake.grow = True
                    score += 1
                    if score >= max_score:
                        victory = True
                        game_over = True
                    try:
                        food.spawn()
                        current_path = []
                        path_lock = False
                    except:
                        game_over = True
                        victory = True

                if game_over:
                    break

        # Draw elements
        if not game_over and current_path:
            draw_laser_path(screen, current_path)
        draw_snake(screen, snake)
        if not victory:
            draw_food(screen, food)

        # UI elements
        score_text = fonts['small'].render(f"Score: {score}/{max_score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        
        speed_button_rect = pygame.Rect(settings['width'] - 150, 10, 140, 40)
        speed_label = f"Speed: {speed_options[current_speed]['label']}"
        draw_button(screen, speed_label, speed_button_rect, speed_button_rect.collidepoint(mouse_pos), fonts['small'])
        
        if show_speed_options:
            for i, option in enumerate(speed_options):
                option_rect = pygame.Rect(
                    speed_button_rect.x,
                    speed_button_rect.y + (i+1)*45,
                    speed_button_rect.width,
                    speed_button_rect.height
                )
                draw_button(screen, option["label"], option_rect, option_rect.collidepoint(mouse_pos), fonts['small'])

        if game_over:
            status_text = "VICTORY!" if victory else "Game Over!"
            color = (50, 205, 50) if victory else TEXT_COLOR
            message = "Perfect Score!" if victory else f"Final Score: {score}"
            
            game_over_text = fonts['large'].render(status_text, True, color)
            screen.blit(game_over_text, (settings['width']//2 - game_over_text.get_width()//2, settings['height']//3))
            
            final_score_text = fonts['medium'].render(message, True, TEXT_COLOR)
            screen.blit(final_score_text, (settings['width']//2 - final_score_text.get_width()//2, settings['height']//2))

            button_y = settings['height'] * 2 // 3
            restart_rect = pygame.Rect(settings['width']//2 - 100, button_y, 200, 40)
            draw_button(screen, "Restart", restart_rect, restart_rect.collidepoint(mouse_pos), fonts['small'])
            
            quit_rect = pygame.Rect(settings['width']//2 - 100, button_y + 60, 200, 40)
            draw_button(screen, "Quit", quit_rect, quit_rect.collidepoint(mouse_pos), fonts['small'])

        # Frame control
        target_fps = base_fps * speed_options[current_speed]["value"] if speed_options[current_speed]["value"] > 0 else 0
        clock.tick(target_fps)
        pygame.display.flip()