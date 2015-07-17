#Battleship! Game

import random

#set up the board
board_length = 10
board = []
for i in range(board_length):
    board.append(["O"]*board_length)

def print_board(board):
    for row in board:
        print row

print_board(board)

#entering random position

#guess_row = int(raw_input("Guess a row: "))
#guess_col = int(raw_input("Guess a column: "))
g = raw_input("Hello: ")

print g
