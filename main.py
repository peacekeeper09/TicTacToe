import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

        self.buttons = [[tk.Button(master, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda row=row, col=col: self.on_click(row, col))
                         for col in range(3)] for row in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

        self.computer_move()

    def on_click(self, row, col):
        if self.board[row][col] == '' and self.current_player == 'X':
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X')
            if self.check_winner():
                messagebox.showinfo("Winner!", "You win!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tie!", "The game is a tie!")
                self.reset_board()
            else:
                self.current_player = 'O'
                self.computer_move()

    def computer_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')
            if self.check_winner():
                messagebox.showinfo("Winner!", "Computer wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tie!", "The game is a tie!")
                self.reset_board()
            else:
                self.current_player = 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ''
                self.buttons[row][col].config(text='')
        self.current_player = 'X'
        self.computer_move()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
