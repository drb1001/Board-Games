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

##SETUP:
computerlevel = 1     #amend for comp difficulty (depth of search)
ishumanfirst = 1      #set to 1 if true, 0 if false

if ishumanfirst==0: iscompfirst=1
else: iscompfirst=0

myboard=board()
titletext="START!"
subtitletext = "Pick computer level (1-7)"
curboardscore = myboard.boardscore
picklevel=True
window,clock=pygamestart()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key in pygamenumbers1to7:
                if picklevel:
                    picklevel = False
                    computerlevel = int(pygame.key.name(event.key))
                    print "Picked comp level %d" %(computerlevel)
                elif myboard.turnnumber%2 == ishumanfirst:
                    humaninput = int(pygame.key.name(event.key))-1
                    if ishumaninputvalid(myboard,humaninput):
                        humanturn(myboard,humaninput)
                        curboardscore = -myboard.boardscore
                        titletext = "COMPUTER TURN!"
                        subtitletext = "..(thinking).."
            if event.key==pygame.K_r:
                titletext = "NEW GAME!"
                subtitletext = "Pick computer level (1-7)"
                picklevel = True
                myboard.resetboard()
                curboardscore = myboard.boardscore

    drawboard(window, myboard)
    drawtitlelabel(window, titletext)
    drawsubtitlelabel(window, subtitletext)
    drawcomplevellabel(window, "Computer level: " + str(computerlevel) )
    drawscorelabel(window, "Board score (you): " + str(curboardscore) )
    pygame.display.flip()
                
    if picklevel:
       pass
    elif myboard.isgameover == False:
            if myboard.turnnumber%2 == iscompfirst:
                computerturn(myboard,computerlevel) #computerlevel = depth of search
                curboardscore = myboard.boardscore
            else:
                titletext="YOUR MOVE!"
                subtitletext="Pick column (1-7)"
    else:
        titletext="GAME OVER!  "
        if myboard.winner == 0:
            titletext2 = "It's a draw!"
        elif myboard.winner + ishumanfirst == 2:
            titletext2 = "You won!"
        else:
            titletext2 = "You lost!"
        titletext = "GAME OVER!" + titletext2      
        subtitletext="(r to restart)"

    drawboard(window, myboard)
    drawtitlelabel(window, titletext)
    drawsubtitlelabel(window, subtitletext)
    drawcomplevellabel(window, "Computer level: " + str(computerlevel) )
    drawscorelabel(window, "Board score (you): " + str(curboardscore) )
    pygame.display.flip()

    # FPS=10
    time_passed = clock.tick(10)
