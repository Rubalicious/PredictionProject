#!/usr/bin/env python

# Connect 4 Game

import numpy as np
import pprint
import subprocess as sp

class C4Game():
    
    def __init__(self):
        # creating a board
        self.board = [[0 for col in range(7)] for row in range(6)]
        self.move_count = 0
        # red player always starts the game
        self.current_player = 1

    def __repr__(self):
        print
        for row in self.board:
            print '\t',
            for entry in row:
                print entry,
            print
        print '\t-------------\n'
        print "\tBoard move: %d \n"% self.move_count

    def move_sequence(self, sequence):
        for x in sequence:
            self.player_move(x)
        
    def player_move(self, col):
        token = self.current_player
        i = 1
        while self.board[-i][col] == 1 or self.board[-i][col] == 2:
            if i > len(self.board[0]):
                print "This column is full!"
                break
            i +=1
        self.board[-i][col] = token
        self.move_count += 1
        self.next_player()

    def next_player(self):
        if self.current_player == 1:
            self.current_player = 2
            return 2
        elif self.current_player == 2:
            self.current_player = 1 
            return 1
    
    def four_in_a_row(self, row, player=1):
        v1 = [player for i in xrange(4)]
        for entry in xrange(len(row)-3):
            v = list(row[entry:entry+4])
            if v == v1:
                return True
        return False

    def four_on_a_diagonal(self, a, player=1):
        v1 = [player for i in xrange(4)]
        x,y = 6,7

        a = np.array(a)
        diags = [a[::-1,:].diagonal(i) for i in xrange(-x+1+3, y-3)]
        diags.extend(a.diagonal(i) for i in xrange(y-1-3, -x+3,-1))

        for el in diags:
            for entry in xrange(len(el)-3):
                v = list(el[entry:entry+4])
                if v == v1:
                    return True

        return False    

    def has_won(self, player):
        won = False
        
        # checking if there exists 4 tokens in any row
        for row in self.board:
            if self.four_in_a_row(row, player):
                won = True
        
        # checking if there exists 4 tokens in any column
        transpose = zip(*self.board)
        for row in transpose:
            if self.four_in_a_row(row, player):
                won = True
        
        # checking if there exists 4 tokens in a diagonal
        if self.four_on_a_diagonal(self.board, player): won = True
        
        return won        
        
                

def main():
    game = C4Game()
    player = game.current_player

    # Welcome to the game
    sp.call('clear', shell=True)
    print 
    print '#######################################'
    print '             CONNECT 4'
    print '#######################################'
    print 'by Ruby Abrams v 1.0'

    while not game.has_won(game.current_player):

        if game.move_count > 41:
            print "It's a tie! Great game!"
            break

        # User interface
        game.__repr__()
        print "It is player %d\'s turn"%game.current_player
        col_num = raw_input("in which column will you place a token? ")

        # Edge cases
        if col_num == 'q': 
            break
        elif not col_num.isdigit():
            sp.call('clear', shell=True)
            print ''
            print '##########################################'
            print '   ERROR: not a digit entry. try again.'
            print '##########################################'
            continue
        elif int(col_num) not in range(7):
            sp.call('clear', shell=True)
            print ''
            print '##########################################'
            print '   ERROR: not a valid entry. try again.'
            print '##########################################'
            continue

        if game.board[0][int(col_num)]:
            sp.call('clear', shell=True)
            print ''
            print '##########################################'
            print '      ERROR: column full. try again'
            print '##########################################'
            continue

        # One person's turn
        game.player_move(int(col_num))
        # sp.call('clear', shell=True)
        
    
    print "Game Over! Player %d won!"%game.current_player

if __name__ == '__main__':
    main()
