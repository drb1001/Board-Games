######################
# Connect 4
# Using [,yellow,red]=[0,1,2]
#
# cols[]rows[]
# 00 01 .. 06
# .. .. .. ..
# 50 51 .. 56
#
######################

import pygame, sys

#1-7 in pygame keypress
pygamenumbers1to7=(pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7)

def pygamestart():
    pygame.init()
    window = pygame.display.set_mode((600, 480))
    pygame.display.set_caption('Connect 4')
    clock = pygame.time.Clock()
    return window,clock

def drawblankboard(window):
    window.fill((255,255,255))
    for j in range(0,7):
        pygame.draw.line(window,(0,0,0),(20,80+60*j),(580,80+60*j))
    for i in range(0,8):
        pygame.draw.line(window,(0,0,0),(20+80*i,80),(20+80*i,440))
    for i in range(0,7):
        myfont = pygame.font.SysFont("monospace", 30)
        label = myfont.render(str(i+1),True,(102,102,102))
        window.blit(label, (20+80*i,78) )

def drawtitlelabel(window,labeltext):
    myfont = pygame.font.SysFont("monospace", 45)
    label = myfont.render(labeltext,True,(0,0,0))
    window.blit(label, (20,5))

def drawsubtitlelabel(window,labeltext):
    myfont = pygame.font.SysFont("monospace", 30)
    label = myfont.render(labeltext,True,(105,105,105))
    window.blit(label, (20,45))

def drawcomplevellabel(window,labeltext):
    myfont = pygame.font.SysFont("monospace", 20)
    label = myfont.render(labeltext,True,(102,102,102))
    window.blit(label, (5,450))

def drawscorelabel(window,labeltext):
    myfont = pygame.font.SysFont("monospace", 20)
    label = myfont.render(labeltext,True,(102,102,102))
    window.blit(label, (310,450))

def drawboard(window,board):
    drawblankboard(window)
    for i in range(0,7):
        for j in range(0,6):
            if board.theboard[i][j].isyellow():
                drawyellowblit(window, (32+80*i,70+60*j) )
            elif board.theboard[i][j].isred():
                drawredblit(window, (32+80*i,70+60*j) )

def drawyellowblit(window,(x,y)):
    myfont = pygame.font.SysFont("monospace", 80)
    label = myfont.render("O",True,(255,225,0))
    window.blit(label, (x,y))

def drawredblit(window,(x,y)):
    myfont = pygame.font.SysFont("monospace", 80)
    label = myfont.render("O",True,(255,0,0))
    window.blit(label, (x,y))
