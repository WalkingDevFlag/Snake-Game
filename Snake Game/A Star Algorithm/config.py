class Config:
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        self.block_size = 20
        self.colors = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'gray': (50, 50, 50),
            'translucent_red': (255, 0, 0, 128)
        }
