# collision_handler.py

def check_collision(snake, width, height):
    # Check for wall collisions
    if snake.x >= width or snake.x < 0 or snake.y >= height or snake.y < 0:
        return True

    # Check for collisions with itself
    for segment in snake.body[:-1]:
        if segment == [snake.x, snake.y]:
            return True

    return False
