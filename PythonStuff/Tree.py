import C4

class Node():

    def __init__(self, state):
        self.state = state
        self.child = None

    def display_tree(self):
        if self.child is None:
            return "*", self.state.__repr__()
        else:
            return "*", display_tree(self.child)

    def add_child(self, state):
        self.child = Node(state)

game = C4.C4Game()
root = Node(game.board)
root.add_child(game.player_move(1))
root.display_tree()
