# Naughts and Crosses
# Using [,X,O]=[0,1,2]

# 123  [0][1][2]
# 456  [3][4][5]
# 789  [6][7][8]

##----------------------

import pygame, sys

#0-8 in pygame keypress
pygamenumbers=(pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9)


def pygamestart():
    pygame.init()
    window = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('Naughts and Crosses')
    clock = pygame.time.Clock()
    return window,clock

def drawblankboard(window):
    window.fill((255,255,255))
    pygame.draw.lines(window,(0,0,0),True,((5,105),(5,695),(595,695),(595,105)), 1)
    pygame.draw.line(window,(0,0,0),(200,110),(200,690))
    pygame.draw.line(window,(0,0,0),(400,110),(400,690))
    pygame.draw.line(window,(0,0,0),(10,300),(590,300))
    pygame.draw.line(window,(0,0,0),(10,500),(590,500))
    for i in range(0,9):
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render(str(i+1),True,(102,102,102))
        (x,y)=(200*(i%3)+30, 200*((i-i%3)/3)+100 )
        window.blit(label,(x,y))

def drawlabel(window,labeltext):
    myfont = pygame.font.SysFont("monospace", 60)
    label = myfont.render(labeltext,True,(0,0,0))
    window.blit(label, (5,5))


def drawboard(window,board):
    drawblankboard(window)
    for i in range(0,9):
        if board.sqs[i].iscross():
            drawXblit(window, ( 200*(i%3)+30, 200*((i-i%3)/3)+100 ))
        elif board.sqs[i].isnaught():
            drawOblit(window, ( 200*(i%3)+30, 200*((i-i%3)/3)+100 ))


def drawXblit(window,(x,y)):
    myfont = pygame.font.SysFont("monospace", 200)
    label = myfont.render("X",True,(255,0,0))
    window.blit(label, (x,y))

def drawOblit(window,(x,y)):
    myfont = pygame.font.SysFont("monospace", 200)
    label = myfont.render("O",True,(0,0,255))
    window.blit(label, (x,y))
