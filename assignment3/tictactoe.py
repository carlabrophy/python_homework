class TictactoeException(Exception):
    """Custom exception for invalid Tic-Tac-Toe moves."""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = []

        lines.append(
            f" {self.board_array[0][0]} | "
            f"{self.board_array[0][1]} | "
            f"{self.board_array[0][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[1][0]} | "
            f"{self.board_array[1][1]} | "
            f"{self.board_array[1][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[2][0]} | "
            f"{self.board_array[2][1]} | "
            f"{self.board_array[2][2]} \n"
        )

        return "".join(lines)

    def move(self, move_string):
        move_string = move_string.lower().strip()

        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)

        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        # Save the player before changing turns
        current_player = self.turn

        self.board_array[row][column] = current_player
        self.last_move = (row, column)

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        # Check all possible winning combinations.
        winning_lines = [
            # Rows
            [
                self.board_array[0][0],
                self.board_array[0][1],
                self.board_array[0][2],
            ],
            [
                self.board_array[1][0],
                self.board_array[1][1],
                self.board_array[1][2],
            ],
            [
                self.board_array[2][0],
                self.board_array[2][1],
                self.board_array[2][2],
            ],

            # Columns
            [
                self.board_array[0][0],
                self.board_array[1][0],
                self.board_array[2][0],
            ],
            [
                self.board_array[0][1],
                self.board_array[1][1],
                self.board_array[2][1],
            ],
            [
                self.board_array[0][2],
                self.board_array[1][2],
                self.board_array[2][2],
            ],

            # Diagonals
            [
                self.board_array[0][0],
                self.board_array[1][1],
                self.board_array[2][2],
            ],
            [
                self.board_array[0][2],
                self.board_array[1][1],
                self.board_array[2][0],
            ],
        ]

        for line in winning_lines:
            if line == ["X", "X", "X"]:
                return True, "X has won"

            if line == ["O", "O", "O"]:
                return True, "O has won"

        # Check whether every square is occupied.
        board_is_full = all(
            space != " "
            for row in self.board_array
            for space in row
        )

        if board_is_full:
            return True, "Cat's Game"

        return False, f"{self.turn}'s turn"


if __name__ == "__main__":
    board = Board()

    print("Welcome to Tic-Tac-Toe!")
    print()
    print("Valid moves are:")
    print(", ".join(Board.valid_moves))
    print()
    print(board)

    game_over = False

    while not game_over:
        game_over, message = board.whats_next()

        if game_over:
            print(message)
            break

        print(message)

        move_choice = input(
            f"{board.turn}, enter your move: "
        )

        try:
            board.move(move_choice)
            print()
            print(board)

        except TictactoeException as error:
            print()
            print(error.message)
            print("Please choose another move.")
            print()