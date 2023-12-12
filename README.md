# Chain Reaction Game with Min-Max AI

Welcome to the Chain Reaction Game with an AI opponent using the Min-Max algorithm with heuristic search!

## Introduction

This project implements the classic Chain Reaction game, enhanced with an AI player that makes strategic moves using the Min-Max algorithm. The game is built in Python and provides an interactive experience for players to enjoy.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [File Structure](#file-structure)
- [AI Algorithm](#ai-algorithm)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- `tabulate` library (install using `pip install tabulate`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chain-reaction-game.git
   cd chain-reaction-game
   ```

2. Run the game:

   ```bash
   python main.py
   ```

## How to Play

1. The game board is represented as an `m x n` grid.
2. Players take turns placing their balls on the grid.
3. The goal is to create chain reactions by placing balls, causing adjacent balls to explode and potentially triggering a cascade effect.
4. The AI player uses the Min-Max algorithm with heuristic search to make strategic moves.

## File Structure

- `game_board.py`: Contains the implementation of the game board and the chain reaction logic.
- `game_operations.py`: Implements game-related operations such as user and computer moves, heuristic functions, and the Min-Max algorithm.
- `main.py`: Entry point of the game.

## AI Algorithm

The AI player utilizes the Min-Max algorithm with heuristic search to make optimal moves. The heuristic function evaluates the current state of the board to guide the AI in making strategic decisions.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and improvements are welcome!
