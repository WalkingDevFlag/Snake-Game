# Snake Game

A classic Snake game implemented in Python using Pygame, divided into modular components for better code organization and maintainability.

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
