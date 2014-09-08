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

from C4setup import *
from C4pygame import *

#Create board class with 7x6 blank squares
board=[]
for i in range(0,7):
    myarray=[]
    for j in range(0,6):
        sq=square(0)
        myarray.append(sq)
    board.append(myarray)

#
humanturn(board,2,1)
humanturn(board,2,1)
#

turncounter=1
humaninput=""
skipcomp=False
labeltext="START GAME!"

window,clock=pygamestart()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key in pygamenumbers1to7:
                if turncounter%2==0:
                    humaninput=int(pygame.key.name(event.key))-1
                    if ishumaninputvalid(board,humaninput):
                        humanturn(board,2,humaninput)
                        turncounter=turncounter+1
                        skipcomp=True
                        labeltext="COMPUTER TURN..."
            if event.key==pygame.K_r:
                resetboard(board)
                turncounter=1
                humaninput=""
                labeltext="RESTART GAME!"
                
    if skipcomp==True:
        skipcomp=False
    else:
        if isgameover(board)==False:
            if turncounter%2==1:
                computerturn(board,2,turncounter,1)
                turncounter=turncounter+1
            else:
                labeltext="YOUR MOVE!"
        else:
            labeltext="GAME OVER! (r)"
    
    drawboard(window, board)
    drawlabel(window, labeltext)
    pygame.display.flip()

    # FPS=10
    time_passed = clock.tick(10)
