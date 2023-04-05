# author: Jan Kwiatkowski
import numpy


class EvaluateFunctions:
    def __init__(self, game_state, is_maximizing_player):
        self.game_state = game_state
        self.is_maximizing_player = is_maximizing_player

    def count_score(self):
        # return self.get_num_free_spaces()
        return self.evaluate_position(self.game_state.board, self.is_maximizing_player)
        # return self.eval_pos_traning(self.game_state.board, self.is_maximizing_player)

    def get_num_free_spaces(self):
        return (self.game_state.board == 0).sum()

    def evaluate_position(self, board, is_maximizing_player):

        # define player pieces and opponent pieces
        if is_maximizing_player:
            my_piece, opp_piece = 1, 2
        else:
            my_piece, opp_piece = 2, 1

        # Define weights for different lengths of continuous lines
        weights = {1: 0.1, 2: 0.3, 3: 0.9}

        # Define middle weights for different board sizes
        middle_weights = {4: 0.5, 5: 0.4, 6: 0.3, 7: 0.2, 8: 0.1}

        # Get middle column index for current board size
        middle_col = len(board[0]) // 2

        # Calculate the number of continuous lines for player and opponent
        my_lines = 0
        opp_lines = 0

        # Check horizontal lines
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                line = board[row][col:col + 4]
                if numpy.count_nonzero(line == my_piece) == 4:
                    return 1  # Maximizer wins
                elif numpy.count_nonzero(line == opp_piece) == 4:
                    return -1  # Minimizer wins
                my_lines += weights.get(numpy.count_nonzero(line == my_piece), 0)
                opp_lines += weights.get(numpy.count_nonzero(line == opp_piece), 0)

        # Check vertical lines
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                line = [board[row + i][col] for i in range(4)]
                if numpy.count_nonzero(line == my_piece) == 4:
                    return 1  # Maximizer wins
                elif numpy.count_nonzero(line == opp_piece) == 4:
                    return -1  # Minimizer wins
                my_lines += weights.get(numpy.count_nonzero(line == my_piece), 0)
                opp_lines += weights.get(numpy.count_nonzero(line == opp_piece), 0)

        # Check diagonal lines (top-left to bottom-right)
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                line = [board[row + i][col + i] for i in range(4)]
                if numpy.count_nonzero(line == my_piece) == 4:
                    return 1  # Maximizer wins
                elif numpy.count_nonzero(line == opp_piece) == 4:
                    return -1  # Minimizer wins
                my_lines += weights.get(numpy.count_nonzero(line == my_piece), 0)
                opp_lines += weights.get(numpy.count_nonzero(line == opp_piece), 0)

        # Check diagonal lines (bottom-left to top-right)
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                line = [board[row + i][col + i] for i in range(4)]
                if line.count(my_piece) == 4:
                    return 1  # Maximizer wins
                elif line.count(opp_piece) == 4:
                    return -1  # Minimizer wins
                my_lines += weights.get(line.count(my_piece), 0)
                opp_lines += weights.get(line.count(opp_piece), 0)

        # Add middle weights for center column
        for row in range(len(board)):
            line = board[row][middle_col]
            if numpy.count_nonzero(line == my_piece) == 1:
                my_lines += middle_weights[len(board)]
            elif numpy.count_nonzero(line == opp_piece) == 1:
                opp_lines += middle_weights[len(board)]

        # Calculate the heuristic value as the difference between my lines and opponent's lines
        return my_lines - opp_lines
