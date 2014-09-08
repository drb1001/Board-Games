# Naughts and Crosses
# Using [,X,O]=[0,1,2]

# 123  [0][1][2]
# 456  [3][4][5]
# 789  [6][7][8]

##----------------------

from OXsetup import *
from OXpygame import *

myboard=board()
labeltext="START GAME!"
window,clock=pygamestart()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key in pygamenumbers:
                if myboard.turnnumber%2==0:
                    humaninput=int(pygame.key.name(event.key))-1
                    if ishumaninputvalid(myboard,humaninput):
                        humanturn(myboard,humaninput)
                        labeltext="COMPUTER TURN..."
            if event.key==pygame.K_r:
                labeltext="RESTART GAME!"
                myboard.resetboard()

    drawboard(window, myboard)
    drawlabel(window, labeltext)
    pygame.display.flip()
                

    if myboard.isgameover == False:
        if myboard.turnnumber%2==1:
            computerturn(myboard)
        else:
            labeltext="YOUR MOVE!"
    else:
       labeltext="GAME OVER! (r)"
    
    drawboard(window, myboard)
    drawlabel(window, labeltext)
    pygame.display.flip()

    # FPS=10
    time_passed = clock.tick(10)
