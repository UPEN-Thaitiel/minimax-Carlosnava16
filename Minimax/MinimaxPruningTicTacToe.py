# Constants for the game setup
BOARD_SIZE = 3       # The Tic-Tac-Toe board is 3x3
REWARD = 10          # Score for winning the game

class TicTacToe:
    def __init__(self, board):
        # Initialize the board dictionary with positions 1-9 as keys
        # 'player' will be human (O), 'computer' is AI (X)
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        # Main game loop
        print("Welcome to Tic-Tac-Toe!")
        print("Computer (X) goes first.")
        self.move_computer()

        while True:
            self.print_board()
            self.move_player()
            if self.check_game_state():
                break
            self.move_computer()
            if self.check_game_state():
                break

    def print_board(self):
        # Display the current board state in 3 rows and 3 columns
        for i in range(1, 10, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 7:
                print("---+---+---")

    def is_cell_free(self, position):
        # Check if the cell at 'position' (1 to 9) is empty (' ')
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        # Place player's mark ('X' or 'O') on the board at 'position'
        if self.is_cell_free(position):
            self.board[position] = player
        else:
            print("Cell is occupied! Choose another position.")
            self.move_player()

    def check_game_state(self):
        # Print the current board
        self.print_board()
        if self.is_winning(self.player):
            print("Player (O) wins!")
            exit()
        elif self.is_winning(self.computer):
            print("Computer (X) wins!")
            exit()
        elif self.is_draw():
            print("Draw!")
            exit()
        return False

    def is_winning(self, player):
        # Check if 'player' ('X' or 'O') has any winning combination
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]               # Diagonals
        ]
        return any(all(self.board[pos] == player for pos in combo) for combo in winning_combinations)

    def is_draw(self):
        # Check if all cells are occupied and no winner
        return all(self.board[pos] != ' ' for pos in range(1, 10)) and not self.is_winning(self.player) and not self.is_winning(self.computer)

    def move_player(self):
        # Ask the human player to input a position (1 to 9)
        while True:
            try:
                position = int(input("Enter your move (1-9): "))
                if position < 1 or position > 9:
                    print("Invalid input! Please enter a number between 1 and 9.")
                else:
                    self.update_player_position(self.player, position)
                    break
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")

    def move_computer(self):
        # Computer chooses best move using Minimax algorithm with alpha-beta pruning
        best_score = float('-inf')
        best_move = None

        for position in range(1, 10):
            if self.is_cell_free(position):
                self.board[position] = self.computer
                score = self.minimax(0, float('-inf'), float('inf'), False)
                self.board[position] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = position

        self.board[best_move] = self.computer
        self.check_game_state()

    def minimax(self, depth, alpha, beta, is_maximizer):
        # Base cases
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0

        if is_maximizer:
            best_score = float('-inf')
            for position in range(1, 10):
                if self.is_cell_free(position):
                    self.board[position] = self.computer
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[position] = ' '  # Undo move
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = float('inf')
            for position in range(1, 10):
                if self.is_cell_free(position):
                    self.board[position] = self.player
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[position] = ' '  # Undo move
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
            return best_score

if __name__ == '__main__':
    # Create empty board dictionary with keys 1 to 9, all set to space ' '
    board = {pos: ' ' for pos in range(1, 10)}

    # Instantiate TicTacToe game with this board
    game = TicTacToe(board)

    # Start the game loop
    game.run()
