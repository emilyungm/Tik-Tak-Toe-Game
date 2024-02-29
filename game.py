import pygame 
from pygame.locals import *


player_char = 'X'

winner = None
draw = False

GAME_WIDTH = 300
GAME_HEIGHT = 300

WHITE = (255, 255, 255)
PINK = (250, 87, 212)
AQUA = (68, 227, 211)
GREY = (237, 235, 235)

LINE_WIDTH = 5

game_board = [[None]*3, [None]*3, [None]*3]

# init pygame window
pygame.init()
pygame.display.set_caption("Tik Tak Toe!")

# game window
screen = pygame.display.set_mode((GAME_WIDTH+50, GAME_HEIGHT+150))
screen.fill(GREY)

# player = pygame.Rect((300, 255, 0, 0))

def draw_game_grid():
    pygame.display.update()

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



# game loop
game_running = True

while game_running:

    draw_game_grid()

    # pygame.draw.rect(screen, (255, 0, 0), player)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    pygame.display.update()

pygame.quit()
