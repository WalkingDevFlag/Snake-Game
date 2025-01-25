from config import GRID_SIZE

class DFSPathfinder:
    def __init__(self, width, height, grid_size):
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Fixed exploration order

    def find_path(self, start, goal, obstacles):
        start_grid = (start[0]//self.grid_size, start[1]//self.grid_size)
        goal_grid = (goal[0]//self.grid_size, goal[1]//self.grid_size)
        obstacles_grid = {(x//self.grid_size, y//self.grid_size) for (x,y) in obstacles}

        stack = [(start_grid, [start_grid])]
        visited = set()
        best_path = None

        while stack:
            current, path = stack.pop()
            
            if current == goal_grid:
                # Track shortest path found
                if not best_path or len(path) < len(best_path):
                    best_path = path
                continue  # Keep searching for potential shorter paths
                
            if current in visited:
                continue
                
            visited.add(current)
            
            # Explore neighbors in consistent order
            for dx, dy in reversed(self.directions):  # Reverse for DFS stack order
                neighbor = (current[0] + dx, current[1] + dy)
                if (0 <= neighbor[0] < self.cols and 
                    0 <= neighbor[1] < self.rows and 
                    neighbor not in obstacles_grid and 
                    neighbor not in visited):
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))

        if best_path:
            # Convert grid coordinates back to pixel positions
            return [(x*self.grid_size, y*self.grid_size) for (x,y) in best_path]
        return None