# Naughts and Crosses
# Using [,X,O]=[0,1,2]

# 123  [0][1][2]
# 456  [3][4][5]
# 789  [6][7][8]

#-----------------------

import random, copy

# square class  - there will be nine of these
class square(object):
    def __init__(self,contents):
        self.contents=contents
    def isempty(self):
        return (self.contents==0)
    def isnotempty(self):
        return (self.contents==1 or self.contents==2) 
    def iscross(self):
        return (self.contents==1)
    def isnaught(self):
        return (self.contents==2)
    def assigncross(self):
        self.contents=1
    def assignnaught(self):
        self.contents=2
    def clearcontents(self):
        self.contents=0


# board class
class board(object):
    
##    currentplayer  # {1,2} = {X,O} Player 1 or 2
##    turnnumber     # {1..9} Turn  
##    winner         # {0,1,2} 0=no winner
##    isgameover     # {T, F} 
##    emptysquares

    def __init__(self):
        self.sqs = []
        for i in range(0,9):
            sq=square(0)
            self.sqs.append(sq)
        self.currentplayer = 1
        self.turnnumber = 1 
        self.winner = 0
        self.isgameover = False   
        self.emptysquares = self.emptysquarescheck()

    def resetboard(self):
        for mysquare in self.sqs:
            mysquare.clearcontents()
        self.currentplayer = 1
        self.turnnumber = 1
        self.winner = 0
        self.isgameover = False
        self.emptysquares = self.emptysquarescheck()
        print "Board reset --------------"
        
    def changeplayer(self):
        if self.currentplayer == 1:
            self.currentplayer = 2
        else:
            self.currentplayer = 1

    def makemove(self,index):
        if self.sqs[index].isempty():
            if self.currentplayer == 1:
                self.sqs[index].assigncross()
            else:
                self.sqs[index].assignnaught()
            self.changeplayer()
            self.turnnumber += 1
            self.winner = self.winnercheck()
            self.isgameover = self.isgameovercheck()
            self.emptysquares = self.emptysquarescheck()

    def emptysquarescheck(self):
        output=[]
        for i in (4,0,2,8,6,1,3,5,7):
            if self.sqs[i].isempty():
                output.append(i)
        return output

    # function to check if there is a winner.
    def winnercheck(self):
        if self.sqs[4].isnotempty():
            for i in [0,1,2,3]:
                if self.sqs[4].contents==self.sqs[i].contents:
                    if self.sqs[4].contents==self.sqs[9-i-1].contents:
                        return self.sqs[4].contents
        for i in [0,6]:
            if self.sqs[i].isnotempty():
                if self.sqs[i].contents==self.sqs[i+1].contents:
                    if self.sqs[i].contents==self.sqs[i+2].contents:
                        return self.sqs[i].contents
        for i in [0,2]:
            if self.sqs[i].isnotempty():
                if self.sqs[i].contents==self.sqs[i+3].contents:
                    if self.sqs[i].contents==self.sqs[i+6].contents:
                        return self.sqs[i].contents
        return 0  #no winner

    #function checks if game is over or not, ie if there is a winner (or full board)
    def isgameovercheck(self):
        if len( self.emptysquarescheck() )==0 or self.winnercheck()!=0:
            return True
        else:
            return False

#-------------------------
        
# check to see if human input is valid for current board
def ishumaninputvalid(board,humaninput):
    if board.isgameover == False:
        if humaninput in board.emptysquares:
            return True
    else:
        return False

# human choice with pygame
def humanturn(board,validhumaninput):
    print str(board.turnnumber)+ " - human move = " + str(validhumaninput+1)
    board.makemove(validhumaninput)
    

#----------------------
  
# computer choice using maximin (random for the first spot)
def computerturn(board):
    turnnumber = board.turnnumber
    available = board.emptysquarescheck()
    if turnnumber == 1:
        pick = random.sample(available,1)[0]
        print str(turnnumber) + " - random choice = " + str(pick+1)
    else:
        (movesequence, minimaxvalue) = minimaxab(board,-10,10)
        pick = movesequence[-1]
        print str(turnnumber) + " - minimax choice = " + str(pick+1) + ".  Minimax value = " + str(minimaxvalue) + ". Next moves = " + str(movesequence)
    board.makemove(pick)

#---------------------

def minimax(board,playersymbol):

    # create list to record move sequence
    movesequence = []
    
    # create a list of available moves (empty squares on board)
    availablemoves = board.emptysquares

    # check to see if game over (there is a winner)
    if board.winner != 0:
        if board.winner == playersymbol:
            return (movesequence,1)
        else:
            return (movesequence,-1)
    # check to see if game over (no more moves = draw)
    elif len(availablemoves) == 0:
        return (movesequence,0)

    # are we checking for computer's turn or opponent's turn (max or min)
    if playersymbol == board.currentplayer:
        newbestscore = lambda x,y: x<y   #maximise moves
        bestscore = -10
    else:
        newbestscore = lambda x,y: x>y   #minimise moves
        bestscore = 10
    
    for move in availablemoves:
        # for all moves create new board and assign relevant symbol
        newboard = copy.deepcopy(board)
        newboard.makemove(move)
        
        # minimax on the newboard
        (newmovesequence, newboardvalue) = minimax(newboard,playersymbol)

        if newbestscore(bestscore,newboardvalue)==True:
            bestscore = newboardvalue
            movesequence = newmovesequence
            movesequence.append(move)

    return (movesequence, bestscore)
      
#---------------------

def minimaxab(board,alpha,beta):

    playersymbol = board.currentplayer
    availablemoves = board.emptysquares
    movesequence = [] # create list to record move sequence
    
    # check to see if game over (there is a winner)
    if board.winner != 0:
        if board.winner == playersymbol:
            return (movesequence,1)
        else:
            return (movesequence,-1)
    # check to see if game over (no more moves = draw)
    elif len(availablemoves) == 0:
        return (movesequence,0)
    
    for move in availablemoves:
        # for all moves create new board and assign relevant symbol
        newboard = copy.deepcopy(board)
        newboard.makemove(move)
        newalpha = -beta
        newbeta = -alpha

        # minimax on the newboard
        (newmovesequence, newboardvalue) = minimaxab(newboard,newalpha,newbeta)
        newboardvalue = -newboardvalue   # switch score between players

        if newboardvalue >= beta:
            return (movesequence,newboardvalue)
        if newboardvalue > alpha:
            alpha = newboardvalue
            movesequence = newmovesequence
            movesequence.append(move)

    return (movesequence, alpha)


#------------------    
##before pygame was implemented
##
##def printbd(board):
##    for i in range(0,3):
##        print str(board[3*i].contents)+ str(board[3*i+1].contents)+str(board[3*i+2].contents)

##def humanturn(board):
##    print "Now it's your go!"
##    x=raw_input("Pick a square - type a number(0 to 8 inclusive)")
##    x=int(x)
##    if x not in range(0,9):
##        print "That's not in range 0 to 8. Try again"
##        humanturn(board)
##    elif not board[x].isempty():
##        print "That square is filled. Try again"
##        humanturn(board)
##    else:
##        board[x].assignnaught
##        print "You choose: " + str(x)

        
#--------------------
## before maximin was implemented

### comp is X=1
##def cancompwin(board):
##    if winstrat(board,1)=="No":
##        print "  Computer has no winning move!"
##        return False
##    else:
##        print "  Computer has found a winning move!"
##        return True
##
### player is O=2
##def cancompblock(board):
##    if winstrat(board,2)=="No":
##        print "  Computer cannot block!"
##        return False
##    else:
##        print "  Computer can block!"
##        return True

# computer choice without using maximin
##def computerchoice(board):
##    if cancompwin(board):
##        return winstrat(board,1)
##    elif cancompblock(board):
##        return winstrat(board,2)
##    else:
##        for i in range(0,9):
##            if board[i].isempty():
##                return i


# function checks to see if there is a winning move to be made
##def winstrat(board,sym):
##    if board[4].contents==sym:
##        for i in range(0,9):
##            if board[i].contents==sym:
##                if board[(9-i-1)%9].isempty():
##                    return (9-i-1)%9
##    for i in [0,6]:
##        if board[i].contents==sym:
##            if board[i+1].contents==sym:
##                if board[i+2].isempty():
##                    return i+2
##            elif board[i+2].contents==sym:
##                if board[i+1].isempty():
##                    return i+1
##    for i in [0,2]:
##        if board[i].contents==sym:
##            if board[i+3].contents==sym:
##                if board[1+6].isempty():
##                    return i+6
##            if board[i+6].contents==sym:
##                if board[1+3].isempty():
##                    return i+3
##    return "No"

