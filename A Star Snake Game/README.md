# A* Pathfinding Snake Game

## Overview
This project implements an AI-driven snake game using the A* pathfinding algorithm. The snake autonomously navigates to find food while avoiding self-collisions, demonstrating optimal pathfinding in grid-based environments.

## Features
- **A* Algorithm**: Uses Manhattan distance heuristic for efficient pathfinding
- **Laser Visualization**: Real-time display of calculated paths
- **Adaptive Speed**: 6 speed levels from 1x to MAX
- **Dynamic Obstacles**: Handles self-collision avoidance
- **Customizable Grid**: Adjustable cell size and window dimensions

## Requirements
- Python 3.8+
- Pygame 2.1.2+
- Windows/macOS/Linux

## Installation
```bash
conda create -n a-star-snake python=3.8 -y
conda activate a-star-snake
pip install pygame
```

## Usage
```bash
Copy
python main.py
```
Mouse controls for speed adjustment and restart

Automatic path recalculation when eating food

## License
MIT License
