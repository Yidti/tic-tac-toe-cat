from tic_tac_toe import TicTacToe
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def tic_tac_toe_cat():
    input('Please Enter to play game: ')
    cls()
    game = TicTacToe()
    game.start()


if __name__ == '__main__':
    tic_tac_toe_cat()
