# main.py
import pygame
from config import default_settings
from menus import main_menu

def main():
    pygame.init()
    settings = default_settings.copy()
    settings['screen'] = pygame.display.set_mode((settings['width'], settings['height']))
    pygame.display.set_caption("Snake Game")
    main_menu(settings)

if __name__ == "__main__":
    main()