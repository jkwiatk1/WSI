# author: Jan Kwiatkowski
# Eksperymenty AI vs AI
from minMaxAlgorithm import MinMax

DEPTH = 4
player1WinsAmount = 0
player2WinsAmount = 0
drawAmount = 0
gamesAmount = 100

for i in range(gamesAmount):
    minmax = MinMax(DEPTH)
    is_maximizing_player = True
    player2_move = None
    while not minmax.game4.is_game_over():
        if is_maximizing_player:
            player1_move = minmax.get_best_move(True)
            print(f"Ruch gracza 1 = {player1_move + 1}")
            move = player1_move
        else:
            player2_move = minmax.get_best_move(False)
            print(f"Ruch gracza 2 = {player2_move + 1}")
            move = player2_move

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
        player1WinsAmount += 1
        print(f"Zwyciężył gracz 1!")
    elif winner == -1:
        player2WinsAmount += 1
        print(f"Zwyciężył gracz 2!")
    else:
        drawAmount += 1
        print("REMIS")

AI_1_winPer = player1WinsAmount / gamesAmount
AI_2_winPer = player2WinsAmount / gamesAmount
drawsPer = drawAmount / gamesAmount
print()
print("WYNIKI DLA GRY AI vs AI")
print(f"Procent wygranych gier przez AI_1: {AI_1_winPer:.2f}")
print(f"Procent wygranych gier przez AI_2: {AI_2_winPer:.2f}")
print(f"Procent remisow: {drawsPer:.2f}")
