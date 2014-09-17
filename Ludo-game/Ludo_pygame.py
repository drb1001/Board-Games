import pygame

def pygamestart():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Ludo')
    clock = pygame.time.Clock()
    clock.tick(0.1)
    return window, clock

def draw_board(window, the_board):
    draw_board_gif()
    draw_pieces()
    draw_dice()
    draw_labels()

window, clock = pygamestart()
clock.tick(1000)