# Naughts and Crosses
# Using [,X,O]=[0,1,2]

# 123  [0][1][2]
# 456  [3][4][5]
# 789  [6][7][8]

##----------------------

from OXsetup import *

# computer choice using maximin (random for the first spot)
def computerturnfullminmax(board, turnnumber, symbol, matches):
    available = emptysquares(board)
    if turnnumber==1:
        pick=4
        print "fixed " + str(turnnumber) + " - " + str(pick)
    elif turnnumber==2:
        if matches in available:
            pick = matches
            print "matches " + str(turnnumber) + " - " + str(pick)
        else:
            pick=available[0]
            print "av[0] " + str(turnnumber) + " - " + str(pick)
    else:
        pick = minimax(board,symbol,symbol)
        pick=pick[0][-1]
        print "minimax " + str(turnnumber) + " - " + str(pick)
    if symbol==1:
        board[pick].assigncross()
    else:
        board[pick].assignnaught()
        

#Create board class with 9 blank squares
board=[]
for i in range(0,9):
    sq=square(0)
    board.append(sq)

gamescores=[0,0,0,0] #(d,x,o,E)

turncounter=1
gameplaying=True

for matches in (0,1):
    print "match " +str(matches)

    while gameplaying:
        
        if turncounter%2==1:
            computerturnfullminmax(board,turncounter,1,matches)
            turncounter=turncounter+1
        else:
            computerturnfullminmax(board,turncounter,2,matches)
            turncounter=turncounter+1

        if isgameover(board):
            gameplaying=False

    w=winner(board)
    if w in (0,1,2):
        gamescores[w]=gamescores[w]+1
    else:
        gamescores[3]=gamescores[3]+1

    printbd(board)
    
    resetboard(board)
    turncounter=1
    gameplaying=True

print "results: " + str(gamescores)
