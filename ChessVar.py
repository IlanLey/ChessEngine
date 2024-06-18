# Name: Ilan Leybman
# GitHub: IlanLey
# Date: May 28th, 2024
# Description: In this chess program, there's a class called ChessVar that acts as the heart of the game.
# It sets up the chessboard, remembers whose turn it is, and keeps tabs on the game's progress.
# Each chess piece, represented by the ChessPiece class and its subclasses like Pawn, Knight,
# and so on, knows its color and how it can move across the board.
# The main part of the program handles everything from setting up the initial board to processing player moves and
# figuring out if the game is still in progress or if someone has won. When you run the program,
# it demonstrates how to play by making moves and showing you the updated board after each move,
# all while keeping track of who's winning.


class ChessVar:
    """
    Represents the state and functionality of a chessboard.
    """

    def __init__(self):
        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self._current_player = "White"
        self._game_state = "UNFINISHED"
        self._pieces = self._initialize_pieces()

    def _initialize_pieces(self):
        """
        Initializes the pieces on the board with their respective classes.
        """
        pieces = {
            'P': Pawn("White"), 'p': Pawn("Black"),
            'R': Rook("White"), 'r': Rook("Black"),
            'N': Knight("White"), 'n': Knight("Black"),
            'B': Bishop("White"), 'b': Bishop("Black"),
            'Q': Queen("White"), 'q': Queen("Black"),
            'K': King("White"), 'k': King("Black")
        }
        return pieces

    def print_board(self):
        """
        Prints the chessboard
        """
        print(" ", " ", "a", "b", "c", "d", "e", "f", "g", "h")
        print(" ", " ", "-", "-", "-", "-", "-", "-", "-", "-")
        for i, row in enumerate(self._board):
            print(f"{8 - i} | {' '.join(row)}")

    def get_game_state(self):
        """
        Returns the current game state.
        """
        return self._game_state

    def set_game_state(self, state):
        """
        Sets the game state.
        """
        self._game_state = state

    def get_current_player(self):
        """
        Returns the current player's turn.
        """
        return self._current_player

    def set_current_player(self, player):
        """
        Sets the current player.
        """
        self._current_player = player

    def get_piece(self, position):
        """
        Returns the piece at the specified position.
        """
        column, row = ord(position[0]) - ord('a'), 8 - int(position[1])
        return self._board[row][column]

    def is_within_bounds(self, position):
        """
        Checks if the position is within the bounds of the chessboard.
        """
        column = ord(position[0]) - ord('a')
        row = 8 - int(position[1])
        return 0 <= column <= 7 and 0 <= row <= 7

    def make_move(self, start, end):
        """
        Moves a chess piece from the start position to the end position if the move is valid.
        """

        # Checks if a move is inside the chessboard limits.
        if not self.is_within_bounds(start) or not self.is_within_bounds(end):
            return False

        # Algebraically notated starting column/row and ending column/row
        start_column = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_column = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        # Print column and row of starting and ending pieces
        """
        print("Start Position (column, row):", start_column, start_row)
        print("Ending Position (column, row):", end_column, end_row)
        """

        # Checks if starting position is empty
        starting_piece, ending_piece = self._board[start_row][start_column], self._board[end_row][end_column]
        if starting_piece == ' ':
            # print("Initial Position is Empty")
            return False

        # Prints the chess piece at the start and end positions.
        """
        print(starting_piece)
        print(ending_piece)
        """

        # Verifies if it is the correct player's turn.
        if (self._current_player == "White" and starting_piece.islower()) or \
                (self._current_player == "Black" and starting_piece.isupper()):
            return False

        # Verifies if the chosen piece can legally make the specified move
        piece = self._pieces[starting_piece]
        if not piece.is_valid_move(start, end, self._board):
            return False

        # Moves pieces around the chessboard
        self._board[start_row][start_column] = ' '
        self._board[end_row][end_column] = starting_piece

        # Sets the current player's turn
        if starting_piece.isupper():
            self.set_current_player("Black")
        else:
            self.set_current_player("White")

        return True


class ChessPiece:
    """
    Represents a generic chess piece with common functionality.
    """

    def __init__(self, color):
        """
        Initializes the color of the chess piece.
        """
        self._color = color

    def get_color(self):
        """
        Returns the color of the chess piece.
        """
        return self._color

    def is_valid_move(self, start, end, board):
        """
        Checks if the move made by a chess piece is valid.
        This method will be inherited by all chess piece classes
        """
        pass


class Pawn(ChessPiece):
    """
    Represents a pawn chess piece.
    """

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        """
        Represents pawn pieces using algebraic notation
        Establishes direction for pawn movements according to their respective color
        Pawns move forward in a straight line and attack diagonally adjacent squares
        """
        start_column = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_column = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        # Sets the direction for pawn movement according to their respective colors
        direction = -1 if self._color == "White" else 1
        starting_row = 6 if self._color == "White" else 1

        if start_column == end_column:
            if start_row + direction == end_row and board[end_row][end_column] == " ":
                return True
            elif start_row == starting_row and end_row == start_row + 2 * direction and \
                    board[end_row][end_column] == " " and board[start_row + direction][start_column] == " ":
                return True

        elif abs(end_column - start_column) == 1 and end_row - start_row == direction:
            if (self._color == "White" and board[end_row][end_column].islower()) or \
                    (self._color == "Black" and board[end_row][end_column].isupper()):
                return True

        return False


class Knight(ChessPiece):
    """
    Represents a knight chess piece.
    """

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        """
        Represents knight pieces using algebraic notation
        Establishes direction for knight movements according to their respective color
        The knight moves and attacks in an L-shaped pattern
        """
        start_column = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_column = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        # The knight possesses a distinctive attack and movement pattern
        possible_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                          (2, 1), (1, 2), (-1, 2), (-2, 1)]

        for move in possible_moves:
            new_column = start_column + move[0]
            new_row = start_row + move[1]
            if new_column == end_column and new_row == end_row:
                if board[end_row][end_column] == ' ' or \
                        (self._color == 'White' and board[end_row][end_column].islower()) or \
                        (self._color == 'Black' and board[end_row][end_column].isupper()):
                    return True
        return False


class Bishop(ChessPiece):
    """
    Represents a bishop chess piece.
    """

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        """
        Represents Bishop pieces using algebraic notation
        Establishes direction for Bishop movements according to their respective color
        The bishop moves diagonally across the chess board
        """
        start_column = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_column = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        column_diff = abs(end_column - start_column)
        row_diff = abs(end_row - start_row)

        if column_diff == row_diff:
            step_column = 1 if end_column > start_column else -1
            step_row = 1 if end_row > start_row else -1

            for step in range(1, column_diff):
                if board[start_row + step * step_row][start_column + step * step_column] != ' ':
                    return False

            if board[end_row][end_column] == ' ' or \
                    (self._color == 'White' and board[end_row][end_column].islower()) or \
                    (self._color == 'Black' and board[end_row][end_column].isupper()):
                return True
        return False


class Rook(ChessPiece):
    """
    Represents a rook chess piece.
    """

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        """
        Represents Rook pieces using algebraic notation
        Establishes direction for Rook movements according to their respective color
        The Rook can move horizontally or vertically across the chess board
        """
        start_column = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_column = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        if start_column == end_column or start_row == end_row:
            step_column = 1 if end_column > start_column else -1 if end_column < start_column else 0
            step_row = 1 if end_row > start_row else -1 if end_row < start_row else 0

            current_column, current_row = start_column + step_column, start_row + step_row

            while current_column != end_column or current_row != end_row:
                if board[current_row][current_column] != ' ':
                    return False
                current_column += step_column
                current_row += step_row

            if board[end_row][end_column] == ' ' or \
                    (self._color == 'White' and board[end_row][end_column].islower()) or \
                    (self._color == 'Black' and board[end_row][end_column].isupper()):
                return True
        return False


class Queen(ChessPiece):
    """
    Represents a queen chess piece.
    """

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        """
        Represents Queen pieces using algebraic notation
        Establishes direction for Queen movements according to their respective color
        The Queen can move horizontally, vertically and diagonally across the chess board
        """

        # Utilizes movement patterns inherited from both the bishop and rook pieces
        bishop = Bishop(self._color)
        rook = Rook(self._color)
        return bishop.is_valid_move(start, end, board) or rook.is_valid_move(start, end, board)


class King(ChessPiece):
    """
    Represents a king chess piece.
    """

    def __init__(self, color):
        super().__init__(color)

    def is_valid_move(self, start, end, board):
        """
        Represents King pieces using algebraic notation
        Establishes direction for King movements according to their respective color
        The king can move one square in any direction around its initial starting position
        """
        start_column = ord(start[0]) - ord('a')
        start_row = 8 - int(start[1])
        end_column = ord(end[0]) - ord('a')
        end_row = 8 - int(end[1])

        column_diff = abs(end_column - start_column)
        row_diff = abs(end_row - start_row)

        if column_diff <= 1 and row_diff <= 1:
            if board[end_row][end_column] == ' ' or \
                    (self._color == 'White' and board[end_row][end_column].islower()) or \
                    (self._color == 'Black' and board[end_row][end_column].isupper()):
                return True
        return False


def main():
    game = ChessVar()
    print(game.make_move('d2', 'd4'))  # output True
    print(game.make_move('g7', 'g5'))  # output True
    print(game.make_move('c1', 'g5'))  # output True
    game.print_board()
    print(game.get_game_state())  # output UNFINISHED


if __name__ == "__main__":
    main()