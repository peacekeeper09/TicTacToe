# TicTacToe
This project is a simple implementation of a Tic Tac Toe game using the Tkinter library in Python, featuring a player-versus-computer gameplay with a basic random move strategy for the computer player.

# Working


https://github.com/PRATIKK0709/TicTacToe/assets/139443204/90abe027-88cd-41c2-859c-2559ec3e0495





# Explaination

### Importing Libraries:
```
import tkinter as tk
from tkinter import messagebox
import random
```
The code starts by importing the necessary libraries: tkinter for GUI, messagebox for displaying message boxes, and random for generating computer moves.

### Class Definition: TicTacToe:
```
class TicTacToe:
    def __init__(self, master):
```
The main class is defined for the Tic Tac Toe game. The constructor (`__init__`) initializes the game by setting up the GUI, creating the game board, and starting the game with the computer making the first move.

### Initialization:
```
self.master.title("Tic Tac Toe")
self.current_player = 'X'
self.board = [['' for _ in range(3)] for _ in range(3)]
```
Initial settings include setting the window title, initializing the current player as 'X', and creating an empty 3x3 game board represented as a list.

### Creating Buttons:
```
self.buttons = [[tk.Button(master, text='', font=('Arial', 24), width=5, height=2,
                           command=lambda row=row, col=col: self.on_click(row, col))
                 for col in range(3)] for row in range(3)]
```
Buttons are created for each cell in the 3x3 grid, and their click events are linked to the on_click method.

### Placing Buttons in the Grid:
```
for row in range(3):
    for col in range(3):
        self.buttons[row][col].grid(row=row, column=col)
```
The buttons are placed in the Tkinter grid layout.

### Starting the Game:
```
self.computer_move()
```
The game starts with the computer making the first move.

### Handling Player Clicks:
```
def on_click(self, row, col):
```
This method is called when a player clicks a button. It checks if the clicked cell is empty for the current player ('X'), updates the board, and checks for a winner or a tie. If neither, it switches to the computer's turn.

### Computer Move:
```
def computer_move(self):
```
The computer makes a move using a simple random strategy. It selects an empty cell randomly, updates the board, and checks for a win or tie.

### Checking for a Winner:
```
def check_winner(self):
```
This method checks for a win by examining rows, columns, and diagonals.

### Checking for a Tie:
```
def is_board_full(self):
```
It checks if the board is full, indicating a tie.

### Resetting the Board:
```
def reset_board(self):
```
This method resets the board for a new game.

### Main Section:
```
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
```
Finally, the script creates an instance of the TicTacToe class, initializing the Tkinter window, and starts the main event loop.


## Summary
In summary, this code defines a basic Tic Tac Toe game with a GUI using Tkinter. Players take turns making moves, and a simple random move strategy is implemented for the computer player. The game checks for a winner or a tie and allows for the reset of the board for a new game.
