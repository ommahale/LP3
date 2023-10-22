def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_queens(board, row):
    if row >= len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack if the current placement doesn't work

    return False

# Initialize an empty chessboard
n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

# Solve the 8-Queens problem starting from the first row
if solve_queens(board, 0):
    print("Solution found:")
    for row in board:
        print(row)
else:
    print("No solution exists.")
