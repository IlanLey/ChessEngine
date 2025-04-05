# ChessEngine

A Python-based chess engine that provides a complete representation of a chess game with move validation and state management.

## Overview

ChessEngine is a Python project that simulates the state and functionality of a chessboard through its ChessVar class. It includes classes for different chess pieces and supports move validation according to standard chess rules. The project provides a foundation for developing chess applications, training AI models, or implementing chess variants.

## Features

- **Chessboard Representation**: Initializes and maintains the state of an 8x8 chessboard
- **Chess Pieces**: Includes classes for Pawn, Knight, Bishop, Rook, Queen, and King with their respective movement rules
- **Move Validation**: Checks the validity of moves based on the type of piece and the rules of chess
- **Turn Management**: Keeps track of the current player's turn

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ChessEngine.git
cd ChessEngine
```

No external dependencies are required - ChessEngine uses standard Python libraries only.

## Usage

```python
from ChessVar import ChessVar

# Initialize a new chess game
game = ChessVar()

# Print the current state of the board
game.print_board()

# Make a move (e.g., move the piece at e2 to e4)
game.make_move("e2", "e4")

# Get the current player
current_player = game.get_current_player()
print(f"Current player: {current_player}")

# Get the current game state
game_state = game.get_game_state()
print(f"Game state: {game_state}")

# Example from the code
print(game.make_move('d2', 'd4'))  # output True
print(game.make_move('g7', 'g5'))  # output True
print(game.make_move('c1', 'g5'))  # output True
```

## Class Structure

### ChessVar

The main class that manages the chess game:

- `__init__`: Initializes the board, current player, game state, and pieces
- `_initialize_pieces`: Internal method to create the chess piece objects
- `print_board`: Prints the current state of the chessboard
- `get_game_state`: Returns the current game state
- `set_game_state`: Sets the game state
- `get_current_player`: Returns the current player
- `set_current_player`: Sets the current player
- `get_piece`: Returns the piece at the specified position
- `is_within_bounds`: Checks if a position is within the bounds of the chessboard
- `make_move`: Moves a piece if the move is valid

### ChessPiece

Base class for all chess pieces:

- `__init__`: Initializes the color of the chess piece
- `get_color`: Returns the color of the chess piece
- `is_valid_move`: Checks if the move made by a chess piece is valid

### Specific Pieces

Each specific piece class inherits from `ChessPiece` and implements the `is_valid_move` method according to that piece's movement rules:

- `Pawn`: Implements forward movement (one or two squares from starting position), diagonal captures
- `Knight`: Implements L-shaped movement (2 squares in one direction + 1 square perpendicular)
- `Bishop`: Implements diagonal movement across any number of squares
- `Rook`: Implements horizontal and vertical movement across any number of squares
- `Queen`: Combines the movement capabilities of Rook and Bishop
- `King`: Implements one-square movement in all directions

The implementation includes proper validation to ensure pieces:
- Cannot move through other pieces (except Knight)
- Can only capture opponent's pieces
- Move according to their specific movement patterns
