BOARD_SIZE = 3
REWARD = 10

class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        while True:
            self.move_computer()
            self.check_game_state()
            self.move_player()
            self.check_game_state()

    def print_board(self):
        print(f"{self.board[1]} | {self.board[2]} | {self.board[3]}")
        print("--+---+--")
        print(f"{self.board[4]} | {self.board[5]} | {self.board[6]}")
        print("--+---+--")
        print(f"{self.board[7]} | {self.board[8]} | {self.board[9]}")

    def is_cell_free(self, position):
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
        else:
            print("Cell is occupied! Try again.")
            self.move_player()

    def is_winning(self, player):
        win_conditions = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
            [1, 5, 9], [3, 5, 7]               # diagonal
        ]
        return any(all(self.board[pos] == player for pos in condition) for condition in win_conditions)

    def is_draw(self):
        return all(self.board[pos] != ' ' for pos in self.board) and not self.is_winning(self.player) and not self.is_winning(self.computer)

    def check_game_state(self):
        self.print_board()
        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()
        elif self.is_winning(self.player):
            print("Player wins!")
            exit()
        elif self.is_draw():
            print("Draw!")
            exit()

    def move_player(self):
        position = int(input("Enter your position (1-9): "))
        if position in self.board and self.is_cell_free(position):
            self.update_player_position(self.player, position)
        else:
            print("Invalid input! Try again.")
            self.move_player()

    def move_computer(self):
        best_score = float('-inf')
        best_move = None
        for position in self.board:
            if self.is_cell_free(position):
                self.board[position] = self.computer
                score = self.minimax(0, False)
                self.board[position] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = position
        self.board[best_move] = self.computer

    def minimax(self, depth, is_maximizer):
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0

        if is_maximizer:
            best_score = float('-inf')
            for position in self.board:
                if self.is_cell_free(position):
                    self.board[position] = self.computer
                    score = self.minimax(depth + 1, False)
                    self.board[position] = ' '  # Undo move
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for position in self.board:
                if self.is_cell_free(position):
                    self.board[position] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[position] = ' '  # Undo move
                    best_score = min(best_score, score)
            return best_score


if __name__ == '__main__':
    board = {pos: ' ' for pos in range(1, 10)}
    game = TicTacToe(board)
    game.run()
