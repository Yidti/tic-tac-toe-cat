import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_table():
    blank_board = ['                                                            \n',
                   '  ┌-------( TicTacToe )-------┬-----( Position No. )-------┐\n',
                   '  │    ┌─────┬─────┬─────┐    │     ┌─────┬─────┬─────┐    │\n',
                   '  │    │     │     │     │    │     │ 1,1 │ 1,2 │ 1,3 │    │\n',
                   '  │    ├─────┼─────┼─────┤    │     ├─────┼─────┼─────┤    │\n',
                   '  │    │     │     │     │    │     │ 2,1 │ 2,2 │ 2,3 │    │\n',
                   '  │    ├─────┼─────┼─────┤    │     ├─────┼─────┼─────┤    │\n',
                   '  │    │     │     │     │    │     │ 3,1 │ 3,2 │ 3,3 │    │\n',
                   '  │    └─────┴─────┴─────┘    │     └─────┴─────┴─────┘    │\n',
                   '  └---------------------------┴----------------------------┘']
    return blank_board


# check input is valid or not
def check_size(_position) -> bool:
    check_false = [False for number in _position if number > 3 or number < 0]
    return False if (False in check_false) else True


# check vertical and horizontal
def vh_three(steps):
    for position in range(1, 4):
        for direction in range(0, 2):
            vh_number = len([step for step in steps if step[direction] == position])
            if vh_number == 3:
                return True


def diagonal_three(steps):
    left_top_right_bottom_number = len([step for step in steps if step[0] == step[1]])
    left_bottom_right_top_number = len([step for step in steps if (step[0] + step[1] == 4)])
    if left_top_right_bottom_number == 3 or left_bottom_right_top_number == 3:
        return True
    else:
        return False


class TicTacToe:

    def __init__(self):
        self.board = []
        self.mark_1 = 'X'
        self.mark_2 = '◯'
        self.winner = ''
        self.turn = self.mark_1
        self.reset_board()
        self.records = []

    def start(self):
        self.show_board()
        while True:
            # print records
            self.print_records()
            # wait input
            _input = input(f"Player '{self.turn}' - key in position: ")
            try:
                _position = tuple(map(int, _input.split(",")))
                print(self.records)
                if check_size(_position) and not self.check_duplicate(_position):
                    # save record
                    self.records.append({self.turn: _position})
                    # making mark
                    self.making_mark(self.turn, _position)
                    # take turns
                    self.turn = self.mark_1 if self.turn != self.mark_1 else self.mark_2
                    # check winner or draw
                    if self.check_winner():
                        self.show_board()
                        self.print_records()
                        print(f"Player '{self.winner}' is winner, Game over")
                        ans = input("Do you wanna play again? (y/n): ")
                        if ans == "y":
                            self.__init__()
                            self.show_board()
                        else:
                            break
                    elif self.check_draw():
                        print(f"The game ended in a draw , Game over")
                        ans = input("Do you wanna play again? (y/n): ")
                        if ans == "y":
                            self.__init__()
                            self.show_board()
                        else:
                            break
                else:
                    self.show_board()

            except ValueError or KeyError:
                self.show_board()

    def check_winner(self):
        mark_1_steps = [list(step.values())[0] for step in self.records if list(step)[0] == self.mark_1]
        mark_2_steps = [list(step.values())[0] for step in self.records if list(step)[0] == self.mark_2]

        if vh_three(mark_1_steps) or diagonal_three(mark_1_steps):
            find_winner = True
            self.winner = self.mark_1
        elif vh_three(mark_2_steps) or diagonal_three(mark_2_steps):
            find_winner = True
            self.winner = self.mark_2
        else:
            find_winner = False

        return find_winner

    def check_draw(self):
        if len(self.records) == 9 and self.winner == '':
            return True
        else:
            return False

    def show_board(self):
        cls()
        print("".join(self.board))

    def reset_board(self):
        self.board = create_table()

    def making_mark(self, player: str, position: tuple):
        dict_position = {
            (1, 1): lambda: self.refresh_line(3, 10, player),
            (1, 2): lambda: self.refresh_line(3, 16, player),
            (1, 3): lambda: self.refresh_line(3, 22, player),
            (2, 1): lambda: self.refresh_line(5, 10, player),
            (2, 2): lambda: self.refresh_line(5, 16, player),
            (2, 3): lambda: self.refresh_line(5, 22, player),
            (3, 1): lambda: self.refresh_line(7, 10, player),
            (3, 2): lambda: self.refresh_line(7, 16, player),
            (3, 3): lambda: self.refresh_line(7, 22, player),
        }
        return dict_position[position]()

    def refresh_line(self, line: int, index: int, insert: str):
        self.board[line] = self.board[line][:index] + insert + self.board[line][index + 1:]
        self.show_board()

    # check input is duplicate or not
    def check_duplicate(self, _position) -> bool:
        check_false = [True for record in self.records if list(record.values())[0] == _position]
        return True if (True in check_false) else False

    def print_records(self):
        print(f"{' -> '.join(map(lambda x: (list(x)[0] + ':' + str(list(x.values())[0])), self.records))}")
