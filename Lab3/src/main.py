from connect4_game import Connect4Game
import random

game4 = Connect4Game()
board = game4.create_board()
game_over = False
turn = 0

# Game Loop
while not game_over:
    if turn == 0:
        player1_move = random.randint(1, game4.COLUMN_AMOUNT)
        print(f"Player 1 move = {player1_move}")
        if game4.is_valid_location(board, player1_move-1):
            row = game4.get_next_row(board, player1_move-1)
            game4.drop_piece(board, row, player1_move-1, game4.PLAYER_1_PIECE)
            turn = 1
            game4.print_board(board)
            if game4.check_is_win(board, game4.PLAYER_1_PIECE):
                print("PLAYER 1 WIN!")
                game_over = True
    else:
        player2_move = random.randint(1, game4.COLUMN_AMOUNT)
        print(f"Player 2 move = {player2_move}")
        if game4.is_valid_location(board, player2_move-1):
            row = game4.get_next_row(board, player2_move-1)
            game4.drop_piece(board, row, player2_move-1, game4.PLAYER_2_PIECE)
            turn = 0
            game4.print_board(board)
            if game4.check_is_win(board, game4.PLAYER_2_PIECE):
                print("PLAYER 2 WIN!")
                game_over = True

    if game4.is_board_full(board):
        print("Game Over: The board is full!")
        game_over = True