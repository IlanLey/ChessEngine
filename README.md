# ChessEngine

# ChessVar

ChessVar is a Python project that simulates the state and functionality of a chessboard. It includes classes for different chess pieces and supports basic move validation according to chess rules.

## Features

- **Chessboard Representation**: Initializes and maintains the state of an 8x8 chessboard.
- **Chess Pieces**: Includes classes for Pawn, Knight, Bishop, Rook, Queen, and King with their respective movement rules.
- **Move Validation**: Checks the validity of moves based on the type of piece and the rules of chess.
- **Turn Management**: Keeps track of the current player's turn.

## Technologies

- Python 3

## Class Overview

### ChessVar

- **`__init__`**: Initializes the board, current player, game state, and pieces.
- **`print_board`**: Prints the current state of the chessboard.
- **`get_game_state`**: Returns the current game state.
- **`set_game_state`**: Sets the game state.
- **`get_current_player`**: Returns the current player.
- **`set_current_player`**: Sets the current player.
- **`get_piece`**: Returns the piece at the specified position.
- **`is_within_bounds`**: Checks if a position is within the bounds of the chessboard.
- **`make_move`**: Moves a piece if the move is valid.

### ChessPiece

- **`__init__`**: Initializes the color of the chess piece.
- **`get_color`**: Returns the color of the chess piece.
- **`is_valid_move`**: Checks if the move made by a chess piece is valid.

### Specific Pieces

Each specific piece class (`Pawn`, `Knight`, `Bishop`, `Rook`, `Queen`, `King`) inherits from `ChessPiece` and implements the `is_valid_move` method according to the movement rules for that piece.
