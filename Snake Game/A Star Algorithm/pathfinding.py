import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal, grid, snake_body):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path = path[::-1]  # Return reversed path
            print("Path found:", path)  # Debug print
            return path

        for neighbor in neighbors:
            neighbor_pos = (current[0] + neighbor[0], current[1] + neighbor[1])
            if (0 <= neighbor_pos[0] < len(grid) and 
                0 <= neighbor_pos[1] < len(grid[0]) and 
                neighbor_pos not in snake_body):
                
                tentative_g_score = g_score[current] + 1
                if neighbor_pos not in g_score or tentative_g_score < g_score[neighbor_pos]:
                    came_from[neighbor_pos] = current
                    g_score[neighbor_pos] = tentative_g_score
                    f_score[neighbor_pos] = tentative_g_score + heuristic(neighbor_pos, goal)
                    heapq.heappush(open_list, (f_score[neighbor_pos], neighbor_pos))

    print("No path found")  # Debug print
    return []  # No path found
