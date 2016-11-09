import unittest
from C4 import C4Game
import sys

class testC4Game(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = C4Game()
        
    @classmethod
    def test_has_won_with_four_horizontal_tokens_on_first_row(self):

        self.game.move_sequence([1,1,2,2,3,3,4])

##        Player 1 won!
##        Board move:  7
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 2 2 2 0 0 0
##        0 1 1 1 1 0 0
##        -------------

        assert self.game.has_won(1)


    @classmethod
    def test_has_won_with_four_horizontal_tokens_on_second_row(self):

        self.game.move_sequence([2,3,4,5,6,5,5,2,2,3,3,4])

##        Player 2 won!
##        Board move:  12
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 1 1 0 1 0
##        0 0 2 2 2 2 0
##        0 0 1 2 1 2 1
##        -------------

        assert self.game.has_won(2), "This returns false"

    @classmethod
    def test_has_won_with_four_vertical_tokens_in_any_column(self):

        self.game.move_sequence([3,4,3,4,3,4,3])

##        Player 1 won!
##        Board move:  7
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 0 1 0 0 0
##        0 0 0 1 2 0 0
##        0 0 0 1 2 0 0
##        0 0 0 1 2 0 0
##        -------------

        assert self.game.has_won(1)

    @classmethod
    def test_has_won_with_four_vertical_tokens_on_second_row(self):

        self.game.move_sequence([4,3,3,4,3,4,3,4,3])

##        Player 1 won!
##        Board move:  9
##        0 0 0 0 0 0 0
##        0 0 0 1 0 0 0
##        0 0 0 1 2 0 0
##        0 0 0 1 2 0 0
##        0 0 0 1 2 0 0
##        0 0 0 2 1 0 0
##        -------------

        assert self.game.has_won(1)


    @classmethod
    def test_has_won_with_four_on_a_diagonal(self):

        self.game.move_sequence([0,1,2,3,1,2,0,1,0,0])

##        Player 2 won!
##        Board move: 10
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        2 0 0 0 0 0 0
##        1 2 0 0 0 0 0
##        1 1 2 0 0 0 0
##        1 2 1 2 0 0 0
##        -------------
        
        assert self.game.has_won(2)


    @classmethod
    def test_that_it_fails(self):

        self.game.move_sequence([0,1,2,3,1,2,0,1,0])

##        Player 2 won!
##        Board move: 10
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        1 2 0 0 0 0 0
##        1 1 2 0 0 0 0
##        1 2 1 2 0 0 0
##        -------------
        
        assert not self.game.has_won(2)

    @classmethod
    def test_four_in_a_row(self):

        # print "==========test four in a row============"
        
        v1 = [0,0,0,1,1,1,1]    # True
        v2 = [0,1,0,1,1,1,1]    # True
        v3 = [0,0,0,1,0,1,1]    # False
        v4 = [0,1,1,1,1,1,1]    # True
        v5 = [0,1,1,1,1,0,0]    # True
        v6 = [2,2,2,2,0,0,0]    # True

        assert self.game.four_in_a_row(v1) 
        assert self.game.four_in_a_row(v2) 
        assert self.game.four_in_a_row(v4) 
        assert self.game.four_in_a_row(v5) 
        assert self.game.four_in_a_row(v6,2) 



    @classmethod
    def test_more_four_in_a_row(self):

        # print "==========test four in a col============"

        M = [(0,0,0,0,0,0,1),
             (0,0,0,0,0,0,1),
             (0,0,0,0,0,1,1),
             (2,0,0,0,2,2,1),
             (1,1,1,2,2,1,1),
             (1,2,2,1,2,1,2)]
        self.board = M

        transpose = zip(*M)
        # v1 = [1 for i in range(4)]
        # v2 = [2 for i in range(4)]
        
        assert self.game.four_in_a_row(transpose[6])
        assert not self.game.four_in_a_row(transpose[5])
        assert not self.game.four_in_a_row(transpose[4])
        assert not self.game.four_in_a_row(transpose[3])
        assert not self.game.four_in_a_row(transpose[2])
        assert not self.game.four_in_a_row(transpose[1])
        assert not self.game.four_in_a_row(transpose[0])

    @classmethod
    def test_four_on_a_diagonal_with_empty_board(self):
        # self.game.__repr__()
        assert not self.game.four_on_a_diagonal(self.game.board)

    @classmethod
    def test_four_on_a_diagonal_with_a_game(self):
        
        assert self.game.current_player == 1
        self.game.player_move(0)
        assert not self.game.has_won(self.game.current_player)
        
        assert self.game.current_player == 2
        self.game.player_move(1) 
        assert self.game.current_player == 1
        assert not self.game.has_won(self.game.current_player)
        
        self.game.player_move(2)
        assert not self.game.has_won(self.game.current_player)
        
        self.game.player_move(3)
        assert not self.game.has_won(self.game.current_player)
        
        self.game.player_move(1)
        assert not self.game.has_won(self.game.current_player)
        
        self.game.player_move(2)
        assert not self.game.has_won(self.game.current_player)
        
        self.game.player_move(0)
        assert not self.game.has_won(self.game.current_player)

        self.game.player_move(1)
        assert not self.game.has_won(self.game.current_player)

        self.game.player_move(0)
        assert not self.game.has_won(self.game.current_player)

        self.game.player_move(0)

##        Player 2 won!
##        Board move: 10
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        2 0 0 0 0 0 0
##        1 2 0 0 0 0 0
##        1 1 2 0 0 0 0
##        1 2 1 2 0 0 0
##        -------------
        
        assert self.game.has_won(2)

    def test_bug_001_game_quits_after_second_move(self):
        self.game.player_move(3)
        assert not self.game.has_won(1)
        self.game.player_move(2)
        assert not self.game.has_won(2)

    def test_bug_002_game_doesnt_quit_on_diagonal_win(self):

        self.game.move_sequence([0,1,2,2,2,4,3,3,4,3,4,3,3,4])

        # Player 2 wins here
            # Board move:  14
            # 0 0 0 0 0 0 0
            # 0 0 0 1 0 0 0
            # 0 0 0 2 2 0 0
            # 0 0 1 2 1 0 0
            # 0 0 2 2 1 0 0
            # 1 2 1 1 2 0 0
            # -------------
        assert self.game.has_won(2)

    def test_bug_003_game_doesnt_quit_immediately(self):
        # it usually takes an extra turn before the game ends
        pass

def main(argv):
    unittest.main(argv=argv, verbosity=2, failfast=False)

if __name__=='__main__':
    unittest.main()
