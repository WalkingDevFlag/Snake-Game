import heapq
from config import GRID_SIZE

class AStarPathfinder:
    def __init__(self, width, height, grid_size):
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_path(self, start, goal, obstacles):
        start_grid = (start[0]//self.grid_size, start[1]//self.grid_size)
        goal_grid = (goal[0]//self.grid_size, goal[1]//self.grid_size)
        obstacles_grid = {(x//self.grid_size, y//self.grid_size) for (x, y) in obstacles}

        open_heap = []
        heapq.heappush(open_heap, (0, start_grid))
        came_from = {}
        g_score = {start_grid: 0}
        f_score = {start_grid: self.heuristic(start_grid, goal_grid)}

        while open_heap:
            current = heapq.heappop(open_heap)[1]

            if current == goal_grid:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return [(x*self.grid_size, y*self.grid_size) for (x, y) in path]

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)

                if 0 <= neighbor[0] < self.cols and 0 <= neighbor[1] < self.rows:
                    if neighbor in obstacles_grid:
                        continue

                    tentative_g = g_score.get(current, float('inf')) + 1
                    if tentative_g < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal_grid)
                        heapq.heappush(open_heap, (f_score[neighbor], neighbor))

        return None