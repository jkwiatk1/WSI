# author: Jan Kwiatkowski
import math
import random

from connect4Game import Connect4Game


class MinMax:
    def __init__(self, depth):
        self.depth = depth
        self.game4 = Connect4Game()

    def min_max(self, game_state, depth, is_maximizing_player=True):
        if depth == 0 or game_state.is_game_over():
            score = game_state.get_score(is_maximizing_player)
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





# TEST
minmax = MinMax(4)
is_maximizing_player = True
player2_move = None
while not minmax.game4.is_game_over():
    if is_maximizing_player:
        player1_move = minmax.get_best_move(True)
        print(f"Player 1 move = {player1_move + 1}")
        move = player1_move
    else:
        do = True
        while do:
            player2_move = random.randint(1, minmax.game4.COLUMN_AMOUNT)
            print(f"Player 2 move = {player2_move}")
            if minmax.game4.is_valid_location(player2_move - 1):
                do = False
        move = player2_move - 1

    row = minmax.game4.get_next_free_row(move)
    if is_maximizing_player:
        minmax.game4.drop_piece(minmax.game4.board, row, move, minmax.game4.PLAYER_1_PIECE)
    elif not is_maximizing_player:
        minmax.game4.drop_piece(minmax.game4.board, row, move, minmax.game4.PLAYER_2_PIECE)
    print(minmax.game4.print_board())
    is_maximizing_player = not is_maximizing_player

#
winner = minmax.game4.get_score(is_maximizing_player=None)
if winner is None:
    print("Remis!")
elif winner == 1:
    print(f"Zwyciężył gracz 1!")
elif winner == -1:
    print(f"Zwyciężył gracz 2!")
else:
    print("REMIS")