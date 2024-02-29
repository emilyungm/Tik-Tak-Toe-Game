import pygame 
from pygame.locals import *
import time


current_player = 'X'

winner = None

GAME_WIDTH = 300
GAME_HEIGHT = 300

SCREEN_WIDTH = GAME_WIDTH + 50
SCREEN_HEIGHT = GAME_HEIGHT + 150

WHITE = (255, 255, 255)
PINK = (250, 87, 212)
AQUA = (68, 227, 211)
GREEN = (75, 209, 113)
GREY = (237, 235, 235)

LINE_WIDTH = 5

game_board = [[None]*3, [None]*3, [None]*3]

round = 0

# init pygame window
pygame.init()
pygame.display.set_caption('Tik Tak Toe!')
pygame.font.init()      # init the font module

# game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(GREY)


def draw_game_grid():
    global current_player, round

    # font for msgs
    calibri_font = pygame.font.SysFont('calibri', 30)

    # display msg to screen
    user_msg = calibri_font.render("It's Player " + current_player + "'s turn!", False, (0, 0, 0))
    text_box = user_msg.get_rect(center=(SCREEN_WIDTH/2, 50))
    screen.blit(user_msg, text_box)

    # white box
    pygame.draw.rect(screen, WHITE, pygame.Rect(25, 100, 300, 300))

    # horizontal lines
    pygame.draw.line(screen, PINK, (25, 100), (325, 100), LINE_WIDTH)
    pygame.draw.line(screen, PINK, (25, 200), (325, 200), LINE_WIDTH)
    pygame.draw.line(screen, PINK, (25, 300), (325, 300), LINE_WIDTH)
    pygame.draw.line(screen, PINK, (25, 400), (325, 400), LINE_WIDTH)

    # vertical lines
    pygame.draw.line(screen, PINK, (25, 100), (25, 400), LINE_WIDTH)
    pygame.draw.line(screen, PINK, (125, 100), (125, 400), LINE_WIDTH)
    pygame.draw.line(screen, PINK, (225, 100), (225, 400), LINE_WIDTH)
    pygame.draw.line(screen, PINK, (325, 100), (325, 400), LINE_WIDTH)

    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col] == 'X':
                pygame.draw.line(screen, AQUA, (col*100 + 40, row*100 + 115), (col*100 + 40 + 73, row*100 + 115 + 73), LINE_WIDTH)
                pygame.draw.line(screen, AQUA, (col*100 + 40 + 73, row*100 + 115), (col*100 + 40, row*100 + 115 + 73), LINE_WIDTH)
            elif game_board[row][col] == 'O':      
                pygame.draw.circle(screen, GREEN, (col*100+40+36,  row*100+115+36), 38, LINE_WIDTH)
                
    # if someone has won, display win message
    if winner:
        # cover up user msg so text can be replaced
        pygame.draw.rect(screen, GREY, (0, 0, SCREEN_WIDTH, 75))
        user_msg = calibri_font.render("Player " + winner + " won!", False, (0, 0, 0))
        text_box = user_msg.get_rect(center=(SCREEN_WIDTH/2, 50))
        screen.blit(user_msg, text_box)

    elif round == 9 and winner is None:
        # cover up user msg so text can be replaced
        pygame.draw.rect(screen, GREY, (0, 0, SCREEN_WIDTH, 75))
        user_msg = calibri_font.render("There was a draw :/", False, (0, 0, 0))
        text_box = user_msg.get_rect(center=(SCREEN_WIDTH/2, 50))
        screen.blit(user_msg, text_box)     

    # update the UI
    pygame.display.update()

    if round == 9 or winner:
        time.sleep(3)
        pygame.quit()

    # cover up user msg so text can be replaced
    pygame.draw.rect(screen, GREY, (0, 0, SCREEN_WIDTH, 75))


def user_interaction_logic():

    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()

        if 110 <= y <= 190:         # row 0
            if 35 <= x <= 115:      # row 0, column 0
                write_player_input_to_grid(0, 0)
            elif 135 < x <= 215:    # row 0, column 1
                write_player_input_to_grid(0, 1)
            elif 235 < x <= 315:    # row 0, column 2
                write_player_input_to_grid(0, 2)

        elif 210 < y <= 290:        # row 1
            if 35 <= x <= 115:      # row 1, column 0
                write_player_input_to_grid(1, 0)
            elif 135 < x <= 215:    # row 1, column 1
                write_player_input_to_grid(1, 1)
            elif 235 < x <= 315:    # row 1, column 2
                write_player_input_to_grid(1, 2)
        
        elif 310 < y <= 390:        # row 2
            if 35 <= x <= 115:      # row 2, column 0
                write_player_input_to_grid(2, 0)
            elif 135 < x <= 215:    # row 2, column 1
                write_player_input_to_grid(2, 1)
            elif 235 < x <= 315:    # row 2, column 2
                write_player_input_to_grid(2, 2)


def write_player_input_to_grid(row_num: int, col_num: int):
    global round, current_player
    if not game_board[row_num][col_num]:            # if the square isn't occupied, let player take it
        game_board[row_num][col_num] = current_player
        round += 1

        if round >= 5:      # game can only be won after 5 turns
            check_winner()

        switch_curr_player()

        
def switch_curr_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def check_winner():
    global winner
    # check for horizontal win
    for row in range(len(game_board)):
        x_count = 0
        o_count = 0

        for col in range(len(game_board)):
            if game_board[row][col] == 'X':
                x_count += 1
            elif game_board[row][col] == 'O':
                o_count += 1
        
        if x_count == 3:
            winner = 'X'
            return
        elif o_count == 3:
            winner = 'O'
            return
        
    # check for vertical win
        for row in range(len(game_board)):
            x_count = 0
            o_count = 0

            for col in range(len(game_board)):
                if game_board[col][row] == 'X':
                    x_count += 1
                elif game_board[col][row] == 'O':
                    o_count += 1
            
            if x_count == 3:
                winner = 'X'
                return
            elif o_count == 3:
                winner = 'O'
                return
            
    # check for diagonal win (left to right)
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        if game_board[0][0] == 'X':
            winner = 'X'
            return
        if game_board[0][0] == 'O':
            winner = 'O'
            return

    # check for diagonal win (right to left)
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        if game_board[0][2] == 'X':
            winner = 'X'
            return
        if game_board[0][2] == 'O':
            winner = 'O'
            return

# game loop
game_running = True

while game_running:

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        else:
            draw_game_grid()
            user_interaction_logic()