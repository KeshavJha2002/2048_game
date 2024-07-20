import random
import keyboard

class Board:

    def __init__(self):
        self.__board = [[0 for j in range(0, 4)] for i in range(0, 4)]

    def print_board(self):
        for row in self.__board:
            print("+-------" * 4 + "+")
            print("|", end="")
            for cell in row:
                print(f"{cell: ^7}|", end="")
            print()
        print("+-------" * 4 + "+")

    @staticmethod
    def __print_prompt():
        print("Commands are as follows:")
        print("'Up arrow key' : Move Up")
        print("'Down arrow key' : Move Down")
        print("'Left arrow key' : Move Left")
        print("'Right arrow key' : Move Right")
        print("Enter your move : ", end='')
        print(flush=True)
        try:
            input_move = Board.get_arrow_key()
            print(input_move)
        except KeyboardInterrupt:
            print("\nExiting the game.")
            exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        return input_move

    @staticmethod
    def get_arrow_key():
      while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up':
                return 'Up'
            elif event.name == 'down':
                return 'Down'
            elif event.name == 'left':
                return 'Left'
            elif event.name == 'right':
                return 'Right'


    def __check_winner_or_loser(self):
        for element in self.__board:
            if element == 2048:
                return "win"
        for i in range(0, 4):
            for j in range(0, 4):
                possible_rows = [i, i - 1, i, i + 1]
                possible_cols = [j - 1, j, j + 1, j]
                for k in range(0, 4):
                    if 0 <= possible_rows[k] < 4 and 0 <= possible_cols[k] < 4:
                        if self.__board[i][j] == self.__board[possible_rows[k]][possible_cols[k]]:
                            return "hold"
        return "loss"

    def __adjust_col(self, col_ind, order):
        if order in {'Up', 'Down'}:
            start, end, step = (0, 4, 1) if order == 'Up' else (3, -1, -1)
            for i in range(start, end, step):
                if self.__board[i][col_ind] != 0:
                    continue
                else:
                    for k in range(i + step, end, step):
                        if self.__board[k][col_ind] != 0:
                            self.__board[i][col_ind], self.__board[k][col_ind] = \
                                self.__board[k][col_ind], self.__board[i][col_ind]
                            break

    def __adjust_row(self, row_ind, order):
        if order in {'Left', 'Right'}:
            start, end, step = (0, 4, 1) if order == 'Left' else (3, -1, -1)
            for j in range(start, end, step):
                if self.__board[row_ind][j] != 0:
                    continue
                else:
                    for k in range(j + step, end, step):
                        if self.__board[row_ind][k] != 0:
                            self.__board[row_ind][j], self.__board[row_ind][k] = \
                                self.__board[row_ind][k], self.__board[row_ind][j]
                            break

    def __generate_value_for_random_position(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.__board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.__board[row][col] = 2

    def __reflect_move(self, input_move):
        if input_move == 'Up':
            for i in range(4):
                self.__adjust_col(i, input_move)
                for j in range(3):
                    if self.__board[j][i] == self.__board[j + 1][i] and self.__board[j][i] != 0:
                        self.__board[j][i] = self.__board[j][i] + self.__board[j + 1][i]
                        self.__board[j + 1][i] = 0
                        self.__adjust_col(i, input_move)
        elif input_move == 'Down':
            for i in range(4):
                self.__adjust_col(i, input_move)
                for j in range(3, -1, -1):
                    if self.__board[j][i] == self.__board[j - 1][i] and self.__board[j][i] != 0:
                        self.__board[j][i] = self.__board[j][i] + self.__board[j - 1][i]
                        self.__board[j - 1][i] = 0
                        self.__adjust_col(i, input_move)
        elif input_move == "Left":
            for i in range(4):
                self.__adjust_row(i, input_move)
                for j in range(3):
                    if self.__board[i][j] == self.__board[i][j + 1] and self.__board[i][j] != 0:
                        self.__board[i][j] = self.__board[i][j] + self.__board[i][j + 1]
                        self.__board[i][j + 1] = 0
                        self.__adjust_row(i, input_move)
        elif input_move == 'Right':
            for i in range(4):
                self.__adjust_row(i, input_move)
                for j in range(3, -1, -1):
                    if self.__board[i][j] == self.__board[i][j - 1] and self.__board[i][j] != 0:
                        self.__board[i][j] = self.__board[i][j] + self.__board[i][j - 1]
                        self.__board[i][j - 1] = 0
                        self.__adjust_row(i, input_move)
        self.__generate_value_for_random_position()

    def move_master(self):
        self.__generate_value_for_random_position()
        self.print_board()
        while True:
            input_move = Board.__print_prompt()
            if input_move is not None:
                self.__reflect_move(input_move)
                self.print_board()
                game_status = self.__check_winner_or_loser()
                if game_status == "hold":
                    continue
                else:
                    if game_status == "win":
                        print("Congratulations!!! You did it.")
                    else:
                        print("Alas!!! You lost. Better luck next time")
                    break

def main():
    board = Board()
    board.move_master()

if __name__ == "__main__":
    main()
