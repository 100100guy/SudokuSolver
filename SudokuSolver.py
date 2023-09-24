import tkinter as tk
from tkinter import ttk  # Import the ttk module

init_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


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
            update_board()

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

    for i in range(3 * box_y, 3 * box_y + 3):
        for j in range(3 * box_x, 3 * box_x + 3):
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


print_board(board)

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
            root, text="", width=6, height=3, font=("Helvetica", 12), bg="white"
        )
        labels[i][j].grid(row=i, column=j)


def solve_sudoku():
    solve(board)
    update_board()


solve_button = tk.Button(root, text="Solve", command=solve_sudoku)
solve_button.grid(row=10, columnspan=9)
update_board()
root.mainloop()
