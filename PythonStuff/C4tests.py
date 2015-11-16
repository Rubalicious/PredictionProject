import unittest
import C4
import sys

class testC4Game(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.game = C4.C4Game()
        
    @classmethod
    def test_has_won_with_four_horizontal_tokens_on_first_row(self):
        self.game.player_move(1)
        self.game.player_move(1)
        self.game.player_move(2)
        self.game.player_move(2)
        self.game.player_move(3)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.__repr__()

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
        print self.game.has_won(1)
        print self.game.has_won(2)

    @classmethod
    def test_has_won_with_four_horizontal_tokens_on_second_row(self):
        self.game.player_move(2)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(5)
        self.game.player_move(6)

        self.game.player_move(5)
        self.game.player_move(5)
        self.game.player_move(2)
        self.game.player_move(2)
        self.game.player_move(3)
        self.game.player_move(3)
        self.game.player_move(4)
        
        self.game.__repr__()

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
        print self.game.has_won(2)
        print self.game.has_won(1)

    @classmethod
    def test_has_won_with_four_vertical_tokens_in_any_column(self):
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(3)

        self.game.__repr__()

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
        print self.game.has_won(1)
        print self.game.has_won(2)

    @classmethod
    def test_has_won_with_four_vertical_tokens_on_second_row(self):
        self.game.player_move(4)
        self.game.player_move(3)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(3)
        self.game.player_move(4)
        self.game.player_move(3)

        self.game.__repr__()

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
        print self.game.has_won(1)
        print self.game.has_won(2)


    @classmethod
    def test_has_won_with_four_on_a_diagonal(self):
        self.game.player_move(0)
        self.game.player_move(1)
        self.game.player_move(2)
        self.game.player_move(3)
        self.game.player_move(1)
        self.game.player_move(2)
        self.game.player_move(0)
        self.game.player_move(1)
        self.game.player_move(0)
        self.game.player_move(0)
        self.game.__repr__()

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
        print self.game.has_won(2)
        print self.game.has_won(1)

    @classmethod
    def test_that_it_fails(self):
        self.game.player_move(0)
        self.game.player_move(1)
        self.game.player_move(2)
        self.game.player_move(3)
        self.game.player_move(1)
        self.game.player_move(2)
        self.game.player_move(0)
        self.game.player_move(1)
        self.game.player_move(0)
        self.game.__repr__()

##        Player 2 won!
##        Board move: 10
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        0 0 0 0 0 0 0
##        1 2 0 0 0 0 0
##        1 1 2 0 0 0 0
##        1 2 1 2 0 0 0
##        -------------
        
        assert self.game.has_won(2)

    @classmethod
    def test_four_in_a_row(self):

        print "==========test four in a row============"
        
        v1 = [0,0,0,1,1,1,1]    # True
        v2 = [0,1,0,1,1,1,1]    # True
        v3 = [0,0,0,1,0,1,1]    # False
        v4 = [0,1,1,1,1,1,1]    # True
        v5 = [0,1,1,1,1,0,0]    # True
        v6 = [2,2,2,2,0,0,0]    # True

        assert self.game.four_in_a_row(v1) 
##        print v1
        assert self.game.four_in_a_row(v2) 
##        print v2
##        self.assertFalse( C4.C4Game.game.four_in_a_row(v3) )
##        print v3
        assert self.game.four_in_a_row(v4) 
##        print v4
        assert self.game.four_in_a_row(v5) 
##        print v5
        assert self.game.four_in_a_row(v6,2) 
##        print v6


    @classmethod
    def test_four_in_a_col(self):

        print "==========test four in a col============"

        M = [(0,0,0,0,0,0,1),
             (0,0,0,0,0,0,1),
             (0,0,0,0,0,1,1),
             (2,0,0,0,2,2,1),
             (1,2,2,1,2,2,2),
             (1,1,1,2,2,1,1),
             (1,2,2,1,2,1,2)]
        self.board = M

        transpose = zip(*M)
        v1 = tuple([1 for i in range(4)])
        v2 = tuple([2 for i in range(4)])
        for j in range(6):
            if (v1 or v2) in transpose[j]:
                assert True

    @classmethod
    def test_four_on_a_diagonal(self):
        assert not self.game.four_on_a_diagonal()

    @classmethod
    def test_a_game(self):
        print 'Testing the game'

        # print self.game.current_player
        self.game.player_move(0) # player 1
        assert not self.game.has_won(self.game.current_player)
        
        # print self.game.current_player
        self.game.player_move(1) # player 2
        print self.game.current_player
        assert not self.game.has_won(self.game.current_player)
        
        print self.game.current_player
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
        self.game.__repr__()

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
        print self.game.has_won(2)
        print self.game.has_won(1)

    # @unittest.expectedFailure("This is a bug")
    def test_bug_001_game_quits_after_second_move(self):
        self.game.player_move(3)
        assert not self.game.has_won(1)
        self.game.player_move(2)
        assert not self.game.has_won(2)

def main(argv):
    unittest.main(argv=argv, verbosity=0, failfast=False)

if __name__=='__main__':
    unittest.main()
