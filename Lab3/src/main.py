from connect4Game import Connect4Game
import random

game4 = Connect4Game()
game_over = False
turn = 0

# Game Loop
while not game_over:
    if turn == 0:
        player1_move = random.randint(1, game4.COLUMN_AMOUNT)
        print(f"Player 1 move = {player1_move}")
        if game4.is_valid_location(player1_move-1):
            row = game4.get_next_row(player1_move-1)
            game4.drop_piece(row, player1_move-1, game4.PLAYER_1_PIECE)
            turn = 1
            game4.print_board()
            if game4.check_is_win(game4.PLAYER_1_PIECE):
                print("PLAYER 1 WIN!")
                game_over = True
    else:
        player2_move = random.randint(1, game4.COLUMN_AMOUNT)
        print(f"Player 2 move = {player2_move}")
        if game4.is_valid_location(player2_move-1):
            row = game4.get_next_row(player2_move-1)
            game4.drop_piece(row, player2_move-1, game4.PLAYER_2_PIECE)
            turn = 0
            game4.print_board()
            if game4.check_is_win(game4.PLAYER_2_PIECE):
                print("PLAYER 2 WIN!")
                game_over = True

    if game4.is_board_full():
        print("Game Over: The board is full!")
        game_over = True