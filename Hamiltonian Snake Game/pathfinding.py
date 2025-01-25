# pathfinding.py
from config import GRID_SIZE

class HamiltonianPath:
    def __init__(self, width, height, grid_size):
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size
        self.path = []
        self.directions = []
        self.generate_cycle()
        
    def generate_cycle(self):
        self.path = []
        for y in range(self.rows):
            if y % 2 == 0:
                for x in range(1, self.cols):
                    self.path.append((x * self.grid_size, y * self.grid_size))
            else:
                for x in reversed(range(1, self.cols)):
                    self.path.append((x * self.grid_size, y * self.grid_size))
        
        last_x, last_y = self.path[-1]
        for x in reversed(range(0, (last_x // self.grid_size) + 1)):
            self.path.append((x * self.grid_size, last_y))
        
        current_y = (last_y // self.grid_size) - 1
        for y in reversed(range(current_y + 1)):
            self.path.append((0, y * self.grid_size))
        
        self.path.append(self.path[0])
        self._create_directions()

    def _create_directions(self):
        self.directions = []
        for i in range(len(self.path)-1):
            px, py = self.path[i]
            cx, cy = self.path[i+1]
            dx = (cx - px) // self.grid_size
            dy = (cy - py) // self.grid_size
            self.directions.append((dx, dy))
        px, py = self.path[-1]
        cx, cy = self.path[0]
        self.directions.append((
            (cx - px) // self.grid_size,
            (cy - py) // self.grid_size
        ))