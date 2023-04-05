# author: Jan Kwiatkowski
# Eksperymenty AI vs random
import random
from minMaxAlgorithm import MinMax

DEPTH = 2
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
        player1WinsAmount += 1
        print(f"Zwyciężył gracz 1!")
    elif winner == -1:
        player2WinsAmount += 1
        print(f"Zwyciężył gracz 2!")
    else:
        drawAmount += 1
        print("REMIS")

AIwinPer = player1WinsAmount / gamesAmount
drawsPer = drawAmount / gamesAmount
randomWinPer = player2WinsAmount / gamesAmount
print()
print("WYNIKI DLA GRY AI vs RANDOM")
print(f"Procent wygranych gier przez AI: {AIwinPer:.2f}")
print(f"Procent wygranych gier przez randoma: {randomWinPer:.2f}")
print(f"Procent remisow: {drawsPer:.2f}")



