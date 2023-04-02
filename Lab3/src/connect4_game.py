import numpy as np

class Connect4Game:
    def __init__(self, row_amount = 4, column_amount = 5):
        self.ROW_AMOUNT = row_amount
        self.COLUMN_AMOUNT = column_amount
        self.PLAYER_1_PIECE = 1
        self.PLAYER_2_PIECE = 2

    def create_board(self):
        board = np.zeros((self.ROW_AMOUNT, self.COLUMN_AMOUNT))
        return board


    def drop_piece(self,board, row, col, piece):
        board[row][col] = piece


    def is_valid_location(self,board, col):
        return board[self.ROW_AMOUNT - 1][col] == 0


    def get_next_row(self,board, col):
        for r in range(self.ROW_AMOUNT):
            if board[r][col] == 0:
                return r


    def print_board(self,board):
        print(np.flip(board, 0))


    def check_is_win(self,board, piece):
        # Check horizontal locations for win
        for c in range(self.COLUMN_AMOUNT - 3):
            for r in range(self.ROW_AMOUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.COLUMN_AMOUNT):
            for r in range(self.ROW_AMOUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(self.COLUMN_AMOUNT - 3):
            for r in range(self.ROW_AMOUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                    c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(self.COLUMN_AMOUNT - 3):
            for r in range(3, self.ROW_AMOUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                    c + 3] == piece:
                    return True

    def is_board_full(self, board):
        return all([not self.is_valid_location(board, i) for i in range(self.COLUMN_AMOUNT)])





