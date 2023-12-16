from enum import Enum


class TicTacToe:

    class TicTacToeState(Enum):
        CROSS_WINS = "CROSS_WINS"
        NOUGHT_WINS = "NOUGHT_WINS"
        TIE = "TIE"
        O = "O"
        X = "X"
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.X = False
        self.O = True
        self.state = TicTacToe.TicTacToeState.X
        self.print_board()

    def print_board(self):
        printed = {None: '_', True: 'O', False: 'X'}
        for row in self.board:
            print(printed[row[0]], printed[row[1]], printed[row[2]])
        print()

    def get_winning_combos(self):
        rows = [self.board[i] for i in range(3)]
        cols = [[self.board[i][j] for i in range(3)] for j in range(3)]
        diagonal1 = [self.board[i][i] for i in range(3)]
        diagonal2 = [self.board[i][2-i] for i in range(3)]

        return *rows, *cols, diagonal1, diagonal2


    def cross(self, x, y):
        if self.board[x][y] is not None:
            raise Exception("Cell is taken")
        self.board[x][y] = self.X
        if [self.X, self.X, self.X] in self.get_winning_combos():
            self.state = TicTacToe.TicTacToeState.CROSS_WINS
        elif any(None in line for line in self.get_winning_combos()):
            self.state = TicTacToe.TicTacToeState.O
        else:
            self.state = TicTacToe.TicTacToeState.TIE
        self.print_board()

    def nought(self, x, y):
        if self.board[x][y] is not None:
            raise Exception("Cell is taken")
        self.board[x][y] = self.O
        if [self.O, self.O, self.O] in self.get_winning_combos():
            self.state = TicTacToe.TicTacToeState.NOUGHT_WINS
        elif any(None in line for line in self.get_winning_combos()):
            self.state = TicTacToe.TicTacToeState.X
        else:
            self.state = TicTacToe.TicTacToeState.TIE
        self.print_board()

    def next(self, x, y):
        if self.state == TicTacToe.TicTacToeState.X: self.cross(x, y)
        elif self.state == TicTacToe.TicTacToeState.O: self.nought(x, y)

if __name__ == "__main__":
    game = TicTacToe()
    while game.state in [TicTacToe.TicTacToeState.X, TicTacToe.TicTacToeState.O]:
        x, y = list(map(int, input().split()))
        try:
            game.next(x, y)
        except:
            print("Invalid move")
    if game.state == TicTacToe.TicTacToeState.TIE:
        print("Draw")
    elif game.state == TicTacToe.TicTacToeState.CROSS_WINS:
        print("X wins")
    else:
        print("O wins")