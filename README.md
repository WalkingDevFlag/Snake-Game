# Snake Games  
**Four unique implementations demonstrating different AI algorithms**

## Overview  
This repository contains four snake game variants, each implementing a different pathfinding approach:  
- **A* Search** - Optimal pathfinding with heuristic  
- **Breadth-First Search (BFS)** - Guaranteed shortest paths  
- **Depth-First Search (DFS)** - Exploratory pathfinding  
- **Hamiltonian Cycle** - Precomputed perfect route  

All implementations share core gameplay mechanics while demonstrating unique algorithmic behaviors.

## Features  

### Common Features  
- Grid-based movement (20px cells)  
- Dynamic food spawning  
- Collision detection (self & boundaries)  
- Speed controls (1x-20x)  
- Score tracking system  
- Pygame visualization  

### Algorithm-Specific Features  
| Implementation | Key Characteristics | Visualization | Path Type |
|----------------|---------------------|---------------|-----------|
| A*             | Manhattan heuristic | Laser path    | Optimal   |
| BFS            | Queue-based         | Laser path    | Shortest  |
| DFS            | Stack-based         | Laser path    | Exploratory |
| Hamiltonian    | Precomputed cycle   | No laser      | Fixed     |

## Requirements  
- Python
- Pygame  

## Installation  
1. Clone repository:  
```bash  
git clone https://github.com/WalkingDevFlag/Snake-Game 
cd pathfinding-snakes  
```  

2. Create conda environment:  
```bash  
conda create -n snake python=3.8 -y  
conda activate snake  
```  

3. Install dependencies:  
```bash  
pip install -r requirements.txt  
```  

## Usage  

### Running Implementations  
```bash  
# A* Search  
python a_star.py  

# BFS  
python bfs.py  

# DFS  
python dfs.py  

# Hamiltonian Cycle  
python hamiltonian.py  
```  


## License  
MIT License 
