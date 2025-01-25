# menus.py
import pygame
import sys
from ui import draw_button, get_fonts
from config import *
from game import game_loop  

def main_menu(settings):
    fonts = get_fonts()
    clock = pygame.time.Clock()
    
    while True:
        screen = settings['screen']
        screen.fill(BG_COLOR)
        mouse_pos = pygame.mouse.get_pos()
        
        title_text = fonts['large'].render("SNAKE AI", True, TEXT_COLOR)
        screen.blit(title_text, (settings['width']//2 - title_text.get_width()//2, settings['height']//4))

        start_rect = pygame.Rect(settings['width']//2 - 100, settings['height']//3, 200, 40)
        draw_button(screen, "Start AI", start_rect, start_rect.collidepoint(mouse_pos), fonts['small'])

        settings_rect = pygame.Rect(settings['width']//2 - 100, settings['height']//3 + 70, 200, 40)
        draw_button(screen, "Settings", settings_rect, settings_rect.collidepoint(mouse_pos), fonts['small'])

        quit_rect = pygame.Rect(settings['width']//2 - 100, settings['height']//3 + 140, 200, 40)
        draw_button(screen, "Quit", quit_rect, quit_rect.collidepoint(mouse_pos), fonts['small'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(mouse_pos):
                    game_loop(settings)
                elif settings_rect.collidepoint(mouse_pos):
                    settings_menu(settings)
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(15)

def settings_menu(settings):
    fonts = get_fonts()
    clock = pygame.time.Clock()
    resolutions = [(800, 600), (1000, 600), (1280, 720)]

    while True:
        screen = settings['screen']
        screen.fill(BG_COLOR)
        mouse_pos = pygame.mouse.get_pos()

        title_text = fonts['large'].render("Settings", True, TEXT_COLOR)
        screen.blit(title_text, (settings['width']//2 - title_text.get_width()//2, settings['height']//8))

        res_text = fonts['medium'].render("Resolution", True, TEXT_COLOR)
        res_rect = res_text.get_rect(center=(settings['width']//2, settings['height']//3))
        screen.blit(res_text, res_rect)

        button_width = 220
        start_y = res_rect.bottom + 30
        for i, res in enumerate(resolutions):
            rect = pygame.Rect(
                settings['width']//2 - button_width//2,
                start_y + i*60,
                button_width,
                40
            )
            text = f"{res[0]}x{res[1]}"
            if res == (settings['width'], settings['height']):
                text += " ✓"
            draw_button(screen, text, rect, rect.collidepoint(mouse_pos), fonts['small'])

        back_rect = pygame.Rect(
            settings['width']//2 - button_width//2,
            settings['height'] - 100,
            button_width,
            40
        )
        draw_button(screen, "Back", back_rect, back_rect.collidepoint(mouse_pos), fonts['small'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, res in enumerate(resolutions):
                    rect = pygame.Rect(
                        settings['width']//2 - button_width//2,
                        start_y + i*60,
                        button_width,
                        40
                    )
                    if rect.collidepoint(mouse_pos):
                        settings['width'], settings['height'] = res
                        settings['screen'] = pygame.display.set_mode(res)
                if back_rect.collidepoint(mouse_pos):
                    return

        pygame.display.flip()
        clock.tick(15)