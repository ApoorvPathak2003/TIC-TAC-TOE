import pygame, sys, numpy

pygame.init()

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("TIC TAC TOE")

RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

LINE_WIDTH = 10
X_WIDTH = 25
X_SPACE = 75
CIRCLE_RADIUS = 75
CIRCLE_WIDTH = 15

BOARD_ROWS = 3
BOARD_COLUMN = 3

board = numpy.zeros((BOARD_ROWS, BOARD_COLUMN))

def draw_lines():
    pygame.draw.line(screen, RED, (0, 300), (900, 300), LINE_WIDTH)
    pygame.draw.line(screen, RED, (0, 600), (900, 600), LINE_WIDTH)

    pygame.draw.line(screen, RED, (300, 0), (300, 900), LINE_WIDTH)
    pygame.draw.line(screen, RED, (600, 0), (600, 900), LINE_WIDTH)

def mark_square(row, column, player):
    board[row][column] = player

def free_square(row, column):
    return board[row][column] == 0

def full_board():
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMN):
            if board[row][column] == 0:
                return False
    
    return True

def x_o_drawing():
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMN):
            if board[row][column] == 1:
                pygame.draw.circle(screen, BLUE, ((column * 300 + 150), (row * 300 + 150)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][column] == 2:
                pygame.draw.line(screen, GREEN, ((column * 300 + X_SPACE), (row * 300 + 300 - X_SPACE)), ((column * 300 + 300 - X_SPACE), (row * 300 + X_SPACE)), X_WIDTH)
                pygame.draw.line(screen, GREEN, ((column * 300 + X_SPACE), (row * 300 + X_SPACE)), ((column * 300 + 150 + X_SPACE), (row * 300 + 150 + X_SPACE)), X_WIDTH)

def check_win(player):
    for column in range(BOARD_COLUMN):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            vertical_win_line(column, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_win_line(row, player)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        top_left_diagonal(player)
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        top_right_diagonal(player)
        return True

    return False


def vertical_win_line(column, player):
    start_ver_line = column * 300 + 150

    if player == 1:
        color = BLUE
    elif player == 2:
        color = GREEN

    pygame.draw.line(screen, color, (start_ver_line, 15), (start_ver_line, 885), 10)

def horizontal_win_line(row, player):
    start_hor_line = row * 300 + 150

    if player == 1:
        color = BLUE
    elif player == 2:
        color = GREEN

    pygame.draw.line(screen, color, (15, start_hor_line), (885 ,start_hor_line), 10)

def top_right_diagonal(player):
    if player == 1:
        color = BLUE
    elif player == 2:
        color = GREEN

    pygame.draw.line(screen, color, (15, 885), (885 ,15), 10)

def top_left_diagonal(player):
    if player == 1:
        color = BLUE
    elif player == 2:
        color = GREEN

    pygame.draw.line(screen, color, (15, 15), (885, 885), 10)

def restart():
    screen.fill("black")
    draw_lines()
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMN):
            board[row][column] = 0

draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            MouseX = event.pos[0]
            MouseY = event.pos[1]

            row_clicked = int(MouseY // 300)
            column_clicked = int(MouseX // 300)

            if free_square(row_clicked, column_clicked):
                mark_square(row_clicked, column_clicked, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                x_o_drawing()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
        
    pygame.display.update()