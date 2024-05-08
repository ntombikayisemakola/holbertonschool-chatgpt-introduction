def print_board(board):
    # Print the current state of the board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            # Get row and column from user input with error handling
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate row and column are within the range 0-2
            if row not in range(3) or col not in range(3):
                print("Invalid row or column. Please enter a value between 0 and 2.")
                continue

            # Check if the cell is already occupied
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place the player's symbol on the board
            board[row][col] = player

            # Check for a winner after the move
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Switch players
            player = "X" if player == "O" else "O"

        except ValueError:
            # Handle non-integer input errors
            print("Invalid input. Please enter a numeric value.")

        except IndexError:
            # Handle out-of-range input errors
            print("Invalid input. Row and column must be between 0 and 2.")


# Start the game
tic_tac_toe()
