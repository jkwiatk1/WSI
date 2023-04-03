# author: Jan Kwiatkowski
import math

from connect4Game import Connect4Game
from evaluateFunction import EvaluateFunctions


class MinMax:
    def __init__(self, depth):
        self.depth = depth
        self.game4 = Connect4Game()
        self.heuristic = EvaluateFunctions()

    def min_max(self, game_state, depth, is_maximizing_player=True):
        if depth == 0 or game_state.is_game_over():
            score = game_state.get_score()
            if score is None:
                score = 0
            return score

        if is_maximizing_player:
            best_score = -math.inf
            for move in game_state.get_possible_moves():
                successor = game_state.get_successor(move, True)
                score = self.min_max(successor, depth - 1, False)
                if score is not None:
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for move in game_state.get_possible_moves():
                successor = game_state.get_successor(move, False)
                score = self.min_max(successor, depth - 1, True)
                if score is not None:
                    best_score = min(best_score, score)
            return best_score

    def get_best_move(self, is_maximizing_player):
        best_move = None
        best_score = float('-inf') if is_maximizing_player else float('inf')
        for move in self.game4.get_possible_moves():
            successor = self.game4.get_successor(move, is_maximizing_player)
            score = self.min_max(successor, self.depth - 1, not is_maximizing_player)
            if is_maximizing_player and score > best_score:
                best_move = move
                best_score = score
            elif not is_maximizing_player and score < best_score:
                best_move = move
                best_score = score
        return best_move

    # def min_max(self, board, depth, is_maximizing_player = True):
    #     if depth == 0 or self.game4.is_board_full():
    #         return self.heuristic.evaluate_position(self.game4.board)
    #     if is_maximizing_player:
    #         best_score = -math.inf
    #         for col in self.game4.get_possible_moves():
    #             row = self.game4.get_next_free_row(col)
    #             game4_new_state = Connect4Game(game4)
    #             new_score = self.game4_new_state.drop_piece(row, col, self.game4.PLAYER_1_PIECE)
    #             score = self.min_max(new_score, depth - 1, False)
    #             best_score = max(best_score, score)
    #         return best_score
    #     else:
    #         best_score = math.inf
    #         for col in self.game4.get_possible_moves():
    #             row = self.game4.get_next_free_row(col)
    #             new_board = self.game4.drop_piece(row, col, self.game4.PLAYER_2_PIECE)
    #             score = self.min_max(new_board, depth - 1, True)
    #             best_score = min(best_score, score)
    #         return best_score

    # def move_min_max(self):
    #     pass

    # def get_best_move(self, board, depth):
    #     best_move = None
    #     best_score = -math.inf
    #     for move in get_possible_moves(board):
    #         new_board = make_move(board, move, "X")
    #         score = minimax(new_board, depth - 1, False)
    #     if score > best_score:
    #         best_score = score
    #     best_move = move
    #     return best_move


minmax = MinMax(3)
is_maximizing_player = True

while not minmax.game4.is_game_over():
    if is_maximizing_player:
        move = minmax.get_best_move(True)
        print(f"Gracz maksymalizujący wykonuje ruch: {move}")
    else:
        move = input("Podaj ruch gracza minimalizującego: ")
    row = minmax.game4.get_next_free_row(move)
    if is_maximizing_player:
        minmax.game4.drop_piece(minmax.game4.board,  row, move, minmax.game4.PLAYER_1_PIECE)
    elif not is_maximizing_player:
        minmax.game4.drop_piece(minmax.game4.board, row, move, minmax.game4.PLAYER_2_PIECE)
    print(minmax.game4.print_board())
    is_maximizing_player = not is_maximizing_player

winner = minmax.game4.get_score()
if winner is None:
    print("Remis!")
elif winner == 1:
    print(f"Zwyciężył gracz 1!")
elif winner == -1:
    print(f"Zwyciężył gracz 2!")
else:
    print("Nie wiem kto wygral czyli REMIS")