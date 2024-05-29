# Snake Game

A classic Snake game implemented in Python using Pygame, divided into modular components for better code organization and maintainability. I will be trying all types of pathfinding algorithms on this board for fun.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a modular implementation of the classic Snake game. The game is built using Python and the Pygame library. The code is divided into multiple modules to enhance readability, maintainability, and scalability.

## Features

- Simple and intuitive controls using the arrow keys.
- Randomly generated food for the snake to eat.
- The snake grows longer as it eats the food.
- Collision detection with walls and the snake's own body.
- Grid background for better visual clarity.
- Modular code structure.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/snake-game.git
    cd snake-game
    ```

2. Install the required dependencies:

    ```sh
    pip install pygame
    ```

## Usage

To start the game, run the `main.py` file:

```sh
python main.py
```

Use the arrow keys to control the snake:

- **Up:** Move up
- **Down:** Move down
- **Left:** Move left
- **Right:** Move right

Press `R` to restart the game after a game over, and `Q` to quit.

## Project Structure
The project is organized into the following files:

```arduino
Copy code
snake-game/
├── config.py
├── input_handler.py
├── collision_handler.py
├── food.py
├── board.py
├── snake.py
├── game.py
└── main.py
```

## Modules

### `main.py`
The entry point for the game. It initializes and starts the game loop.

### `config.py`
Contains configuration constants such as screen dimensions, block size, and color definitions.

### `input_handler.py`
Handles user input and updates the snake's direction based on key presses.

### `collision_handler.py`
Contains functions for detecting collisions with the walls and the snake's own body.

### `food.py`
Manages the food's behavior, including generating new positions and drawing the food on the screen.

### `board.py`
Handles the game board's appearance, including drawing the grid and managing the background.

### `snake.py`
Defines the Snake class, which includes methods for updating the snake's position, drawing it on the screen, and handling growth.

### `game.py`
Contains the main game logic, including the game loop, initializing components, handling game states, and rendering all elements on the screen.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

Lmao no License

