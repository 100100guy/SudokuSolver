import tkinter as tk
import random
import copy
from tkinter import ttk  # Import the ttk module

init_board = [[0 for _ in range(9)] for _ in range(9)]

board = [[0 for _ in range(9)] for _ in range(9)]


def generate_sudoku():
    # Fill diagonal subgrids
    fill_diagonal_subgrid(board)
    # Solve the Sudoku
    solve(board)
    # Adjust the number of empty cells as needed
    empty_cells = random.sample(range(81), 45)

    for cell in empty_cells:
        row, col = divmod(cell, 9)
        board[row][col] = 0


def fill_diagonal_subgrid(board):
    for k in range(0, 9, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[k + i][k + j] = nums.pop()


def solve(bo):
    find = empty_field(bo)
    if not find:
        return True
    else:
        r, c = find
    for num in range(1, 10):
        if is_valid_move(bo, r, c, num):
            bo[r][c] = num
            # print_board(bo)
            # print()

            if solve(bo):
                return True

            bo[r][c] = 0

    return False


def is_valid_move(bo, row, col, num):
    # check row
    for i in range(len(bo[0])):
        if bo[row][i] == num and i != col:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][col] == num and i != row:
            return False

    # Check box
    box_x = col // 3
    box_y = row // 3

    for i in range(3*box_y, 3*box_y+3):
        for j in range(3*box_x, 3*box_x+3):
            if bo[i][j] == num and i != row and j != col:
                return False

    return True


def empty_field(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


def print_board(bo):
    for row in range(len(bo)):
        if row % 3 == 0:
            print("- - - - - - - - - - - - - ")
        for col in range(len(bo[0])):
            if col % 3 == 0:
                print("| ", end="")
            print(bo[row][col], end=" ")
        print("|")
    print("- - - - - - - - - - - - - ")


generate_sudoku()
print_board(board)
init_board = copy.deepcopy(board)
print_board(init_board)

# Create a tkinter window
root = tk.Tk()
root.title("Sudoku Solver")


def update_board():
    for i in range(9):
        for j in range(9):
            value = board[i][j]
            if value != 0:
                if board[i][j] == init_board[i][j]:
                    labels[i][j].config(text=str(value), fg="red")
                else:
                    labels[i][j].config(text=str(value))
            else:
                labels[i][j].config(text="")


labels = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        labels[i][j] = tk.Button(
            root, text="", width=6, height=3, font=("Helvetica", 12), bg="white")
        labels[i][j].grid(row=i, column=j)


def solve_sudoku():
    solve(board)
    update_board()


solve_button = tk.Button(root, text="Solve", command=solve_sudoku)
solve_button.grid(row=10, columnspan=9)
update_board()
root.mainloop()
