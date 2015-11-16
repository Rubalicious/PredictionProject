#!/usr/bin/env python

# Connect 4 Game

import numpy as np
import pprint

class C4Game():
    
    def __init__(self):
        # creating a board
        self.board = [[0 for col in range(7)] for row in range(6)]
        self.move_count = 0
        # red player always starts the game
        self.current_player = 1

    def __repr__(self):
        print "\nBoard move: ", self.move_count
        for row in self.board:
            for entry in row:
                print entry,
            print
        print '-------------\n'

    def player_move(self, col):
        token = self.current_player
        i = 1
        while self.board[-i][col] == 1 or self.board[-i][col] == 2:
            if i > len(self.board[0]):
                print "This column is full!"
                break
            i +=1
        self.board[-i][col] = token
##        print "number of spaces taken column ",col,": ",i
        self.move_count += 1
        self.next_player()

    def next_player(self):
        if self.current_player == 1:
            self.current_player = 2
            return 2
        elif self.current_player == 2:
            self.current_player = 1 
            return 1

    def has_won(self, player):
        won = False
        
        # checking if there exists 4 tokens in any row
        
        for row in self.board:
            if self.four_in_a_row(row, player):
                won = True
        
        # checking if there exists 4 tokens in any column
        transpose = zip(*self.board)
        for row in transpose:
            if self.four_in_a_col(row, player):
                won = True
        
        # checking if there exists 4 tokens in a diagonal
                
        if self.four_on_a_diagonal(player): won = True
        

        return won
    
    def four_in_a_row(self, row, player=1):
        v1 = [player for i in xrange(4)]
        for entry in xrange(4):
            v = row[entry:entry+4]
            if v == v1 and player in v1:
                return True
        return False

    def four_in_a_col(self, col, player=1):
        v1 = tuple([player for i in xrange(4)])
        for entry in xrange(3):
            v = col[entry:entry+4]
            if v == v1 and player in v1:
                return True
        return False

    def four_on_a_diagonal(self, player=1):
        v1 = tuple([player for i in xrange(4)])
        x,y = 6,7
        a = np.arange(x*y).reshape(x,y)
        for i in xrange(x):
            for j in xrange(y):
                a[i][j] = self.board[i][j]

        diags = [a[::-1,:].diagonal(i) for i in xrange(-a.shape[0]+1, a.shape[1])]
        diags.extend(a.diagonal(i) for i in xrange(a.shape[1]-1, -a.shape[0],-1))
##        diags = [el for el in diags if len(el) >= 4]
        for el in diags:
            if v1 in el and player in v1:
                return True
##        pprint.pprint( [n.tolist() for n in diags] ) 
        return False            
        
                

def main():
    game = C4Game()
    # game.__repr__()
    player = game.current_player
    # end = False
    while game.has_won(player) is False:
        if game.move_count > 41:
            print "It's a tie! Great game!"
            break
        game.__repr__()
        print "It is your turn, player", player
        col_num = raw_input("in which column will you place a token? ")
        if col_num == 'q': 
            break
        game.player_move(int(col_num))
        if game.has_won(player): end = True
        player = game.next_player()
        
    print "Game Over!"


main()
# print "imported"
