# author: Jan Kwiatkowski
import numpy as np

from evaluateFunction import EvaluateFunctions


class Connect4Game:
    def __init__(self, board=[], row_amount=4, column_amount=5):
        self.ROW_AMOUNT = row_amount
        self.COLUMN_AMOUNT = column_amount
        self.PLAYER_1_PIECE = 1
        self.PLAYER_2_PIECE = 2
        self.board = board
        if len(board) == 0:
            self.board = self.create_board()
        elif len(board) != 0:
            self.board = board

    def create_board(self):
        board = np.zeros((self.ROW_AMOUNT, self.COLUMN_AMOUNT))
        return board

    # def copy_board(self):
    #     return [row[:] for row in self.board]

    def get_successor(self, move, is_maximizing_player):
        piece = self.PLAYER_1_PIECE if is_maximizing_player else self.PLAYER_2_PIECE
        row = self.get_next_free_row(move)
        new_game_state = Connect4Game(board=self.board.copy())
        new_game_state.drop_piece(new_game_state.board,row, move, piece)
        return new_game_state

    def get_score(self):
        """
        Metoda zwraca wartość związaną z wynikiem gry:
        1 dla wygranej gracza X
        -1 dla wygranej gracza O
        0 dla remisu lub nierozstrzygniętej gry
        """
        if self.check_is_win(self.PLAYER_1_PIECE):
            return 1
        elif self.check_is_win(self.PLAYER_2_PIECE):
            return -1
        elif self.is_board_full():
            return 0
        else:
            score = EvaluateFunctions(self).count_score()
            return score
            # return None

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[self.ROW_AMOUNT - 1][col] == 0

    def get_next_free_row(self, col):
        for r in range(self.ROW_AMOUNT):
            if self.board[r][col] == 0:
                return r

    def get_possible_moves(self):
        possible_locations = []
        for col in range(self.COLUMN_AMOUNT):
            if self.is_valid_location(col):
                possible_locations.append(col)
        return possible_locations

    def print_board(self):
        print(np.flip(self.board, 0))

    def check_is_win(self, piece):
        # Sprawdzenie zwycięzcy w wierszach
        for c in range(self.COLUMN_AMOUNT - 3):
            for r in range(self.ROW_AMOUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and \
                        self.board[r][c + 3] == piece:
                    return True

        # Sprawdzenie zwycięzcy w kolumnach
        for c in range(self.COLUMN_AMOUNT):
            for r in range(self.ROW_AMOUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece:
                    return True

        # Sprawdzenie zwycięzcy na ukos w prawo-górę
        for c in range(self.COLUMN_AMOUNT - 3):
            for r in range(self.ROW_AMOUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][
                    c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Sprawdzenie zwycięzcy na ukos w lewo-górę
        for c in range(self.COLUMN_AMOUNT - 3):
            for r in range(3, self.ROW_AMOUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][
                    c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

        # Brak
        return None

    def is_board_full(self):
        return all([not self.is_valid_location(i) for i in range(self.COLUMN_AMOUNT)])

    def is_game_over(self):
        if self.check_is_win(self.PLAYER_1_PIECE) or self.check_is_win(self.PLAYER_2_PIECE):
            return True
        if len(self.get_possible_moves()) == 0:
            return True
        return False