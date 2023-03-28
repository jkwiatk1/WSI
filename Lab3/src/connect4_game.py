import pygame
import numpy as np
import sys
import math

"""
https://analityk.edu.pl/pygame-wprowadzenie/
"""

# ustalanie rozmiarów planszy
ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)

# ustalanie kolorów
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#
# # tworzenie planszy
# def create_board():
#     board = [[0 for x in range(COLUMN_COUNT)] for y in range(ROW_COUNT)]
#     return board
#
# # wprowadzanie ruchu
# def drop_piece(board, row, col, piece):
#     board[row][col] = piece
#
# def is_valid_location(board, col):
#     return board[ROW_COUNT - 1][col] == 0
#
# def get_next_open_row(board, col):
#     for r in range(ROW_COUNT):
#         if board[r][col] == 0:
#             return r
#
# def print_board(board):
#     print(np.flip(board, 0))
#
# # sprawdzanie, czy ktoś wygrał
# def winning_move(board, piece):
#     # sprawdzanie poziomej wygranej
#     for c in range(COLUMN_COUNT-3):
#         for r in range(ROW_COUNT):
#             if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
#                 return True
#
#     # sprawdzanie pionowej wygranej
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT-3):
#             if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
#                 return True
#
#     # sprawdzanie wygranej na ukos
#     for c in range(COLUMN_COUNT-3):
#         for r in range(ROW_COUNT-3):
#             if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
#                 return True
#
#     for c in range(COLUMN_COUNT-3):
#         for r in range(3, ROW_COUNT):
#             if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
#                 return True
#
# # rysowanie planszy
# def draw_board(board):
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT):
#             pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
#             pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
#
#     for c in range(COLUMN_COUNT):
#         for r in range(ROW_COUNT):
#             if board[r][c] == 1:
#                 pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
#             elif board[r][c] == 2:
#                 pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
#     pygame.display.update()

# główna funkcja gry
def connect_four():
    # deklarowanie kolorów
    CZERWONY = (255, 0, 0)
    ZIELONY = (0, 255, 0)
    ZOLTY = (255, 255, 0)
    FIOLETOWY = (128, 0, 128)
    JASNY_NIEBIESKI = (0, 255, 255)
    POMARANCZOWY = (255, 165, 0)
    NIEBIESKI = (0, 0, 255)
    SZARY = (128, 128, 128)

    pygame.init()
    # definiowanie okna gry
    win = pygame.display.set_mode((500, 500))
    # wyświetlenie okna gry
    pygame.display.set_caption("Moja Gra")
    run = True
    # pętla główna
    while run:
        # obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.draw.circle(win, (128, 0, 128), (60, 200), 50, 0)
        # linia pozioma
        pygame.draw.line(win, NIEBIESKI, (10, 325), (110, 325), 15)
        # linia pionowa
        pygame.draw.line(win, SZARY, (210, 275), (210, 375), 5)
        # odświeżenie ekranu
        pygame.display.update()

connect_four()


