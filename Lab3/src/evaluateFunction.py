# author: Jan Kwiatkowski
import numpy as np

class EvaluateFunctions:
    def __init__(self, game_state):
        self.game_state = game_state

    def count_score(self):
        return self.get_num_free_spaces()

    def get_num_free_spaces(self):
        return (self.game_state.board == 0).sum()
    def evaluate_position(self,board, player):
        pass

    # def evaluate_position(self,board, player):
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