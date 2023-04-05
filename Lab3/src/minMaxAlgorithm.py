# author: Jan Kwiatkowski
import math

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