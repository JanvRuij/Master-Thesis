import numpy as np

def is_valid(board, row, col, num):
    """Check if it's valid to place the number in the given position."""
    # Check the row
    if num in board[row, :]:
        return False
    
    # Check the column
    if num in board[:, col]:
        return False
    
    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_pos = find_empty_position(board)
    if not empty_pos:
        return True  # Puzzle solved
    
    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num
            if solve_sudoku(board):
                return True
            board[row, col] = 0  # Backtrack
    
    return False

def find_empty_position(board):
    """Find an empty position (represented by 0) in the board."""
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return (i, j)
    return None

# Example usage with one of the provided puzzles
z = np.array([
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 7, 3, 0, 2, 6, 0, 0],
    [0, 0, 3, 0, 0, 5, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 9, 0, 0, 3, 0, 0],
    [0, 0, 5, 2, 0, 6, 7, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [9, 1, 0, 0, 0, 0, 0, 0, 0]
])

if solve_sudoku(z):
    print("Solved Sudoku:\n", z)
else:
    print("No solution exists.")
