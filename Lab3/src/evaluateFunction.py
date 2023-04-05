# author: Jan Kwiatkowski
import numpy


class EvaluateFunctions:
    def __init__(self, game_state, is_maximizing_player):
        self.game_state = game_state
        self.is_maximizing_player = is_maximizing_player

    def count_score(self):
        return self.evaluate_position(self.game_state.board, self.is_maximizing_player)

    def evaluate_position(self, board, is_maximizing_player):

        if is_maximizing_player:
            my_piece, opp_piece = 1, 2
        else:
            my_piece, opp_piece = 2, 1

        weights = {1: 0.1, 2: 0.3, 3: 0.9}

        middle_weights = {4: 0.5, 5: 0.4, 6: 0.3, 7: 0.2, 8: 0.1}

        middle_col = len(board[0]) // 2

        my_lines = 0
        opp_lines = 0

        # poziome
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                line = board[row][col:col + 4]
                if numpy.count_nonzero(line == my_piece) == 4:
                    return 1  # Max wins
                elif numpy.count_nonzero(line == opp_piece) == 4:
                    return -1  # Min wins
                my_lines += weights.get(numpy.count_nonzero(line == my_piece), 0)
                opp_lines += weights.get(numpy.count_nonzero(line == opp_piece), 0)

        # Pionowe
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                line = [board[row + i][col] for i in range(4)]
                if numpy.count_nonzero(line == my_piece) == 4:
                    return 1
                elif numpy.count_nonzero(line == opp_piece) == 4:
                    return -1
                my_lines += weights.get(numpy.count_nonzero(line == my_piece), 0)
                opp_lines += weights.get(numpy.count_nonzero(line == opp_piece), 0)

        # Na ukos (gora-lewo -> dol-prawo)
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                line = [board[row + i][col + i] for i in range(4)]
                if numpy.count_nonzero(line == my_piece) == 4:
                    return 1
                elif numpy.count_nonzero(line == opp_piece) == 4:
                    return -1
                my_lines += weights.get(numpy.count_nonzero(line == my_piece), 0)
                opp_lines += weights.get(numpy.count_nonzero(line == opp_piece), 0)

        # Na ukos (dol-lewo -> gora-prawo)
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                line = [board[row + i][col + i] for i in range(4)]
                if line.count(my_piece) == 4:
                    return 1  # Maximizer wins
                elif line.count(opp_piece) == 4:
                    return -1  # Minimizer wins
                my_lines += weights.get(line.count(my_piece), 0)
                opp_lines += weights.get(line.count(opp_piece), 0)

        # wagi dla srodkowej kolumny
        for row in range(len(board)):
            line = board[row][middle_col]
            if numpy.count_nonzero(line == my_piece) == 1:
                my_lines += middle_weights[len(board)]
            elif numpy.count_nonzero(line == opp_piece) == 1:
                opp_lines += middle_weights[len(board)]

        # Wartość heurystyczną jako różnicę między znormalizowaną do 1 liczba lini player1 a liczba lini player2
        return my_lines - opp_lines
