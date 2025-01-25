import pygame
import sys
from entities import Snake, Food
from pathfinding import AStarPathfinder
from ui import draw_snake, draw_food, draw_button, draw_grid, draw_laser_path, get_fonts
from config import *

def game_loop(settings):
    screen = settings['screen']
    fonts = get_fonts()
    clock = pygame.time.Clock()
    grid_surface = draw_grid(settings['width'], settings['height'])
    
    # Initialize game components
    pathfinder = AStarPathfinder(settings['width'], settings['height'], GRID_SIZE)
    snake = Snake(settings['width'], settings['height'])
    food = Food(settings['width'], settings['height'], snake)
    
    # Game state variables
    current_path = []
    score = 0
    running = True
    game_over = False
    victory = False
    show_speed_options = False
    base_fps = 15
    current_speed = 0

    # Calculate maximum possible score
    total_cells = (settings['width'] // GRID_SIZE) * (settings['height'] // GRID_SIZE)
    max_score = total_cells - 1  # Subtract initial snake length

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

        # Game logic
        if not game_over:
            moves = speed_options[current_speed]["moves"]
            for _ in range(moves):
                # Calculate path to food
                current_path = pathfinder.find_path(
                    snake.body[0], 
                    food.position,
                    snake.body_set
                )
                
                if not current_path:
                    game_over = True
                    break
                
                # Get direction from path
                next_node = current_path[0]
                dx = (next_node[0] - snake.body[0][0]) // GRID_SIZE
                dy = (next_node[1] - snake.body[0][1]) // GRID_SIZE
                snake.direction = (dx, dy)

                # Move snake
                collision = snake.move()
                
                # Boundary checking
                head_x, head_y = snake.body[0]
                boundary_collision = (
                    head_x < 0 or head_x >= settings['width'] or
                    head_y < 0 or head_y >= settings['height']
                )
                
                # Check victory condition
                if score >= max_score:
                    game_over = True
                    victory = True
                    break

                # Update game over state
                game_over = boundary_collision or collision

                # Food handling
                if snake.body[0] == food.position:
                    snake.grow = True
                    score += 1
                    try:
                        food.spawn()
                    except:
                        game_over = True
                        victory = True

                if game_over:
                    break

        # Draw laser path first
        if not game_over and current_path:
            draw_laser_path(screen, current_path)

        # Then draw snake and food
        draw_snake(screen, snake)
        if not victory:
            draw_food(screen, food)

        # UI Elements
        score_text = fonts['small'].render(f"Score: {score}/{max_score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        
        # Speed control UI
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
            # Game over screen
            if victory:
                game_over_text = fonts['large'].render("VICTORY!", True, (50, 205, 50))
                message = "Perfect Score!"
            else:
                game_over_text = fonts['large'].render("Game Over!", True, TEXT_COLOR)
                message = f"Final Score: {score}"
            
            screen.blit(game_over_text, (settings['width']//2 - game_over_text.get_width()//2, settings['height']//3))
            final_score_text = fonts['medium'].render(message, True, TEXT_COLOR)
            screen.blit(final_score_text, (settings['width']//2 - final_score_text.get_width()//2, settings['height']//2))

            # Restart button
            restart_rect = pygame.Rect(settings['width']//2 - 100, settings['height']*2//3, 200, 40)
            draw_button(screen, "Restart (SPACE)", restart_rect, restart_rect.collidepoint(mouse_pos), fonts['small'])

            # Quit button
            quit_rect = pygame.Rect(settings['width']//2 - 100, settings['height']*2//3 + 60, 200, 40)
            draw_button(screen, "Quit", quit_rect, quit_rect.collidepoint(mouse_pos), fonts['small'])

        # Frame rate control
        target_fps = base_fps * speed_options[current_speed]["value"] if speed_options[current_speed]["value"] > 0 else 0
        clock.tick(target_fps)
        pygame.display.flip()