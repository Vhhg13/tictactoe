import unittest


class TicTacToeTest(unittest.TestCase):

    def test_game_X_wins(self):
        game = TicTacToe()
        game.cross(0, 0)
        game.nought(1, 1)
        game.cross(0, 1)
        game.nought(1, 2)
        game.cross(0, 2)
        self.assertEquals(game.state, TicTacToe.TicTacToeState.CROSS_WINS)

    def test_game_O_wins(self):
        game = TicTacToe()
        game.cross(0, 0)
        game.nought(1, 1)
        game.cross(2, 2)
        game.nought(1, 0)
        game.cross(2, 1)
        game.nought(1, 2)
        self.assertEquals(game.state, TicTacToe.TicTacToeState.NOUGHT_WINS)

    def test_draw(self):
        game = TicTacToe()
        game.cross(0, 0)
        game.nought(0, 1)
        game.cross(0, 2)

        game.nought(2, 0)
        game.cross(2, 1)
        game.nought(2, 2)

        game.cross(1, 0)
        game.nought(1, 1)
        game.nought(1, 2)

        self.assertEquals(game.state, TicTacToe.TicTacToeState.TIE)


    def test_X_goes_first(self):
        game = TicTacToe()
        try:
            game.nought(0, 0)
            self.fail("O was able to go first")
        except:
            pass


    def test_X_cant_go_after_X(self):
        game = TicTacToe()
        game.cross(0, 0)
        try:
            game.cross(0, 1)
            self.fail("X was able to make a move twice")
        except:
            pass

    def test_O_cant_go_after_O(self):
        game = TicTacToe()
        game.cross(0, 0)
        game.nought(0, 1)
        try:
            game.nought(0, 2)
            self.fail("O was able to make a move twice")
        except:
            pass

    def test_X_cant_take_a_taken_cell(self):
        game = TicTacToe()
        game.cross(0, 0)
        try:
            game.cross(0, 0)
            self.fail("X was able to take a taken cell")
        except:
            pass

    def test_O_cant_take_a_taken_cell(self):
        game = TicTacToe()
        game.cross(0, 0)
        try:
            game.nought(0, 0)
            self.fail("O was able to take a taken cell")
        except:
            pass


if __name__ == '__main__':
    unittest.main()
