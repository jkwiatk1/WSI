# author: Jan Kwiatkowski
# Gra dla dwoch graczy grajacych losowo
import random

from connect4Game import Connect4Game

game4 = Connect4Game(row_amount=5, column_amount=5)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        player1_move = random.randint(1, game4.COLUMN_AMOUNT)
        print(f"Ruch gracza 1 = {player1_move}")
        if game4.is_valid_location(player1_move - 1):
            row = game4.get_next_free_row(player1_move - 1)
            game4.drop_piece(game4.board,row, player1_move - 1, game4.PLAYER_1_PIECE)
            turn = 1
            game4.print_board()
            print()
            if game4.check_is_win(game4.PLAYER_1_PIECE):
                print("GRACZ 1 wygrał!")
                game_over = True
    else:
        player2_move = random.randint(1, game4.COLUMN_AMOUNT)
        print(f"Ruch gracza 2 = {player2_move}")
        if game4.is_valid_location(player2_move - 1):
            row = game4.get_next_free_row(player2_move - 1)
            game4.drop_piece(game4.board,row, player2_move - 1, game4.PLAYER_2_PIECE)
            turn = 0
            game4.print_board()
            print()
            if game4.check_is_win(game4.PLAYER_2_PIECE):
                print("GRACZ 2 wygrał!")
                game_over = True

    if game4.is_board_full():
        print("Koniec: Tablica jest pełna! REMIS")
        game_over = True
