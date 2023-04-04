# author: Jan Kwiatkowski
import numpy

class EvaluateFunctions:
    def __init__(self, game_state,is_maximizing_player):
        self.game_state = game_state
        self.is_maximizing_player = is_maximizing_player

    def count_score(self):
        # return self.get_num_free_spaces()
        return self.evaluate_position(self.game_state.board,self.is_maximizing_player)
        # return self.eval_pos_traning(self.game_state.board, self.is_maximizing_player)

    def get_num_free_spaces(self):
        return (self.game_state.board == 0).sum()



    def evaluate_position(self,board, is_maximizing_player):

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

        # if line.count(my_piece) == 4:
        #     return 1  # Maximizer wins
        # elif line.count(opp_piece) == 4:
        #     return -1  # Minimizer wins

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



    # def evaluate_window(self, window, piece):
    #     PLAYER_PIECE = 1
    #     AI_PIECE = 2
    #     score = 0
    #     opp_piece = PLAYER_PIECE
    #     if piece == PLAYER_PIECE:
    #         opp_piece = AI_PIECE
    #
    #     if window.count(piece) == 4:
    #         score += 100
    #     elif window.count(piece) == 3 and window.count(EMPTY) == 1:
    #         score += 5
    #     elif window.count(piece) == 2 and window.count(EMPTY) == 2:
    #         score += 2
    #
    #     if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
    #         score -= 4
    #
    #     return score
    #
    # def eval_pos_traning(self, board, is_maximizing_player):
    #     ROW_COUNT = 6
    #     COLUMN_COUNT = 7
    #     WINDOW_LENGTH = 4
    #     if is_maximizing_player:
    #         piece = 1
    #     else:
    #         piece = 2
    #
    #     score = 0
    #
    #     ## Score center column
    #     center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    #     center_count = center_array.count(piece)
    #     score += center_count * 3
    #
    #     ## Score Horizontal
    #     for r in range(ROW_COUNT):
    #         row_array = [int(i) for i in list(board[r, :])]
    #         for c in range(COLUMN_COUNT - 3):
    #             window = row_array[c:c + WINDOW_LENGTH]
    #             score += self.evaluate_window(window, piece)
    #
    #     ## Score Vertical
    #     for c in range(COLUMN_COUNT):
    #         col_array = [int(i) for i in list(board[:, c])]
    #         for r in range(ROW_COUNT - 3):
    #             window = col_array[r:r + WINDOW_LENGTH]
    #             score += self.evaluate_window(window, piece)
    #
    #     ## Score posiive sloped diagonal
    #     for r in range(ROW_COUNT - 3):
    #         for c in range(COLUMN_COUNT - 3):
    #             window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
    #             score += self.evaluate_window(window, piece)
    #
    #     for r in range(ROW_COUNT - 3):
    #         for c in range(COLUMN_COUNT - 3):
    #             window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
    #             score += self.evaluate_window(window, piece)
    #
    #     return score









                #     # heurystyki
    #     score = 0
    #
    #     # heurystyka 1: liczba możliwych czterech w rzędzie
    #     '''
    #     Liczba możliwych czterech w rzędzie: w tej heurystyce oblicza się,
    #     ile możliwych czterech pionków można ułożyć w rzędzie w danym stanie planszy.
    #     Im więcej możliwości, tym lepsza pozycja.
    #     '''
    #     possible_wins = 0
    #     for i in range(board.shape[0]):
    #         for j in range(board.shape[1]):
    #             if board[i][j] == 0:
    #                 for k in [-1, 0, 1]:
    #                     for l in [-1, 0, 1]:
    #                         if k == l == 0:
    #                             continue
    #                         if i + k < 0 or i + k >= board.shape[0] or j + l < 0 or j + l >= board.shape[1]:
    #                             continue
    #                         if board[i + k][j + l] != 0:
    #                             continue
    #                         if self.count_wins_in_direction(board, player, i, j, k, l) > 0:
    #                             possible_wins += 1
    #     score += possible_wins
    #
    #
    #     # heurystyka 2: liczba pionków w rzędach
    #     '''
    #     Liczba pionków w rzędach: w tej heurystyce oblicza się,
    #     ile pionków jest już ułożonych w rzędach (poziomych, pionowych i skośnych) w danym stanie planszy.
    #     Im więcej pionków w rzędach, tym lepsza pozycja.
    #     '''
    #     for i in range(board.shape[0]):
    #         for j in range(board.shape[1]):
    #             if board[i][j] == player:
    #                 for k in [-1, 0, 1]:
    #                     for l in [-1, 0, 1]:
    #                         if k == l == 0:
    #                             continue
    #                         if i + k < 0 or i + k >= board.shape[0] or j + l < 0 or j + l >= board.shape[1]:
    #                             continue
    #                         if board[i + k][j + l] == player:
    #                             score += 1
    #
    #
    #     # heurystyka 3: liczba otwartych przestrzeni
    #     '''
    #     Liczba otwartych przestrzeni: w tej heurystyce oblicza się,
    #     ile otwartych przestrzeni (wolnych pól) pozostało na planszy w danym stanie.
    #     Im więcej otwartych przestrzeni, tym lepsza pozycja.
    #     '''
    #     open_spaces = np.sum(board == 0)
    #     score += open_spaces
    #
    #
    #     # heurystyka 4: liczba blokad
    #     '''
    #     Liczba blokad: w tej heurystyce oblicza się, ile blokad (pustych pól między pionkami) pozostało na planszy w danym stanie.
    #     Im mniej blokad, tym lepsza pozycja.
    #     '''
    #     blocks = np.sum((board[1:] != 0) & (board[:-1] != 0))
    #     score -= blocks
    #
    #
    #     # heurystyka 5: liczba pionków wokół pola centralnego
    #     '''
    #     Liczba pionków wokół pola centralnego: w tej heurystyce oblicza się,
    #     ile pionków znajduje się wokół pola centralnego planszy.
    #     To pole jest ważne, ponieważ daje możliwość ułożenia czterech pionków w rzędzie w różnych kierunkach.
    #     Im więcej pionków wokół pola centralnego, tym lepsza pozycja.
    #     '''
    #     central_field = board[3][3]
    #     if central_field == player:
    #         score += np.sum(board[2:5, 2:5] == player)
    #     else:
    #         score -= np.sum(board[2:5, 2:5] == player)
    #
    #     return score
    #
    # def count_wins_in_direction(self, board, player, row, col, d_row, d_col):
    #     count = 0
    #     for i in range(1, 4):
    #         r = row + i * d_row
    #         c = col + i * d_col
    #         if r < 0 or r >= board.shape[0] or c < 0 or c >= board.shape[1]:
    #             break
    #         if board[r][c] != player:
    #             break
    #         count += 1
    #     return count