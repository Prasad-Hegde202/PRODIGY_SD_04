
def is_valid(board, row, col, num):
    
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(board):
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers 1 to 9 in the empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  

                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If the current placement leads to no solution, backtrack
                        board[row][col] = 0

                return False  # No valid number found, trigger backtracking

    return True  # Solved successfully

# Function to print the Sudoku board
def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Function to get Sudoku puzzle input from the user
def get_user_input():
    board = []
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
    for i in range(9):
        while True:
            row = input(f"Enter row {i+1} (9 digits, use 0 for empty cells): ")
            if len(row) == 9 and row.isdigit():
                board.append([int(digit) for digit in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits.")
    return board

# Main function
def main():
    # Get the Sudoku puzzle from the user
    sudoku_board = get_user_input()

    # Solving the Sudoku puzzle
    if solve_sudoku(sudoku_board):
        print("\nSudoku solved successfully!")
        print_sudoku(sudoku_board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
