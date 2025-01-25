from collections import deque
from config import GRID_SIZE

class BFSPathfinder:
    def __init__(self, width, height, grid_size):
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size

    def find_path(self, start, goal, obstacles):
        start_grid = (start[0]//self.grid_size, start[1]//self.grid_size)
        goal_grid = (goal[0]//self.grid_size, goal[1]//self.grid_size)
        obstacles_grid = {(x//self.grid_size, y//self.grid_size) for (x,y) in obstacles}

        queue = deque()
        queue.append(start_grid)
        came_from = {}
        visited = set()
        visited.add(start_grid)

        while queue:
            current = queue.popleft()

            if current == goal_grid:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return [(x*self.grid_size, y*self.grid_size) for (x,y) in path]

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)

                if (0 <= neighbor[0] < self.cols and 
                    0 <= neighbor[1] < self.rows and 
                    neighbor not in visited and 
                    neighbor not in obstacles_grid):
                    
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return None