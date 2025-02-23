# PRODIGY_SD_04

Task 4: Sudoku Solver
This repository contains a Python program that solves Sudoku puzzles using the backtracking algorithm. The user can input an unsolved Sudoku puzzle, and the program will automatically solve it by filling in the missing numbers.

Features:
User Input: The program prompts the user to input the Sudoku puzzle row by row (using 0 for empty cells).
Backtracking Algorithm: The solver uses the backtracking technique to explore possible solutions and fill in the correct numbers.
Solution Output: Once solved, the program displays the completed Sudoku grid.

Usage:
Clone the repository to your local machine.
Run the Python script sudoku_solver.py.
Enter the Sudoku puzzle row by row when prompted, using 0 to represent empty cells.
The program will output the solved Sudoku grid or notify you if no solution exists

Example:
Enter row 1 (9 digits, use 0 for empty cells): 530070000
Enter row 2 (9 digits, use 0 for empty cells): 600195000
Enter row 3 (9 digits, use 0 for empty cells): 098000060
...
Solved Sudoku:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
...
Requirements:
Python 3.12.1
