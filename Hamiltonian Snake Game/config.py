# config.py
GRID_SIZE = 20
BG_COLOR = (25, 25, 25)
SNAKE_COLOR = (0, 255, 127)
FOOD_COLOR = (255, 50, 50)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 150, 200)

default_settings = {
    'width': 800,
    'height': 600,
    'screen': None
}

speed_options = [
    {"label": "1x", "value": 1, "moves": 1},
    {"label": "2x", "value": 2, "moves": 1},
    {"label": "5x", "value": 5, "moves": 2},
    {"label": "10x", "value": 10, "moves": 5},
    {"label": "20x", "value": 20, "moves": 10},
    {"label": "50x", "value": 50, "moves": 50},
    {"label": "MAX", "value": 0, "moves": 100}
]