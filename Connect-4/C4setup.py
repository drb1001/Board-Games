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

import random, copy

# square class  - there will be nine of these
class square(object):
    def __init__(self,contents):
        self.contents=contents
    def isempty(self):
        return (self.contents==0)
    def isnotempty(self):
        return (self.contents==1 or self.contents==2) 
    def isyellow(self):
        return (self.contents==1)
    def isred(self):
        return (self.contents==2)
    def assignyellow(self):
        self.contents=1
    def assignred(self):
        self.contents=2
    def clearcontents(self):
        self.contents=0

#------------------------

# board class
class board(object):
    
##    currentplayer  # {1,2} = {X,O} Player 1 or 2
##    turnnumber     # {1..42} Turn  
##    winner         # {0,1,2} 0=no winner
##    isgameover     # {T, F}
##    availablecols
##    availablesqs
##    boardscore

    def __init__(self):
        self.theboard=[]
        for i in range(0,7):
            myarray=[]
            for j in range(0,6):
                sq=square(0)
                myarray.append(sq)
            self.theboard.append(myarray)
        self.currentplayer = 1
        self.turnnumber = 1 
        self.winner = 0
        self.isgameover = False
        self.availablecols = self.availablecolscheck()
        self.availablesqs = self.availablesqscheck()
        self.boardscore = self.calcboardscore()

    def resetboard(self):
        print "reset-----------------"
        for i in range(0,7):
            for j in range(0,6):
                self.theboard[i][j].clearcontents()
        self.currentplayer = 1
        self.turnnumber = 1
        self.winner = 0
        self.isgameover = False
        self.availablecols = self.availablecolscheck()
        self.availablesqs = self.availablesqscheck()
        self.boardscore = 0
       
    def changeplayer(self):
        if self.currentplayer == 1:
            self.currentplayer = 2
        else:
            self.currentplayer = 1
            
    #----
            
    # outputs a list of available columns (in order of preference)
    def availablecolscheck(self):
        output=[]
        for i in (3,4,2,1,5,6,0):
            if self.theboard[i][0].isempty():
                output.append(i)
        return output

    # finds point where disc drops to in certain non-full column
    def finddrop(self,availablecolumn):
        for i in range(5,-1,-1):
            if self.theboard[availablecolumn][i].isempty():
                return i

    # finds available squares to place counter
    def availablesqscheck(self):
        output=[]
        avcols = self.availablecolscheck()
        if len(avcols) == 0:
            return output
        else:
            for column in avcols:
                row = self.finddrop(column)
                output.append([column,row])
            return output

    #----
        
    def makemove(self,col,row):
        if self.theboard[col][row].isempty():
            if self.currentplayer == 1:
                self.theboard[col][row].assignyellow()
            else:
                self.theboard[col][row].assignred()
            self.changeplayer()
            self.turnnumber += 1
            self.winner = self.winnercheck()
            self.isgameover = self.isgameovercheck()
            self.availablecols = self.availablecolscheck()
            self.availablesqs = self.availablesqscheck()
            self.boardscore = self.calcboardscore()

    #----
            
    # function to check if there is a winner.
    def winnercheck(self):
        # check rows
        for row in range(0,6):
            for start in range(0,4):
                checkstr=""
                for i in range(0,4):
                    checkstr+=str(self.theboard[start+i][row].contents)
                if checkstr=="2222":
                    return 2
                elif checkstr=="1111":
                    return 1
        # check cols
        for col in range(0,7):
            for start in range(0,3):
                checkstr=""
                for i in range(0,4):
                    checkstr+=str(self.theboard[col][start+i].contents)
                if checkstr=="2222":
                    return 2
                elif checkstr=="1111":
                    return 1
        # check \ diagonals
        for col in range(0,4):
               for start in range(0,3):
                checkstr=""
                for i in range(0,4):
                    checkstr+=str(self.theboard[col+i][start+i].contents)
                if checkstr=="2222":
                    return 2
                elif checkstr=="1111":
                    return 1
                
        # check / diagonals
        for col in range(3,7):
             for start in range(0,3):
                checkstr=""
                for i in range(0,4):
                    checkstr+=str(self.theboard[col-i][start+i].contents)
                if checkstr=="2222":
                    return 2
                elif checkstr=="1111":
                    return 1
        # else
        return 0


    #function checks if game is over or not, ie if there is a winner (or full board)
    def isgameovercheck(self):
        if len( self.availablecolscheck() )==0 or self.winnercheck()!=0:
            return True
        else:
            return False

    #----
        
    def boardscoreplay1(self):
        if self.winner != 0:
            if self.winner == 1:  return 10000
            else: return -10000
            
        runningtotal=0
        # check rows
        for row in range(0,6):
            for start in range(0,4):
                checkstr = ""
                for i in range(0,4):
                    checkstr = checkstr + str(self.theboard[start+i][row].contents)
                if checkstr in self.scoredict:
                    runningtotal = runningtotal + self.scoredict[checkstr]
                    
        # check cols
        for col in range(0,7):
            for start in range(0,3):
                checkstr = ""
                for i in range(0,4):
                    checkstr = checkstr + str(self.theboard[col][start+i].contents)
                if checkstr in self.scoredict:
                    runningtotal = runningtotal + self.scoredict[checkstr]

        # check \ diagonals
        for col in range(0,4):
               for start in range(0,3):
                checkstr = ""
                for i in range(0,4):
                    checkstr = checkstr + str(self.theboard[col+i][start+i].contents)
                if checkstr in self.scoredict:
                    runningtotal = runningtotal + self.scoredict[checkstr]
                    
        # check / diagonals
        for col in range(3,7):
             for start in range(0,3):
                checkstr = ""
                for i in range(0,4):
                    checkstr = checkstr + str(self.theboard[col-i][start+i].contents)
                if checkstr in self.scoredict:
                    runningtotal = runningtotal + self.scoredict[checkstr]
        return runningtotal            

    def calcboardscore(self):
        if self.currentplayer == 1:
            return self.boardscoreplay1()
        elif self.currentplayer == 2:
            return -self.boardscoreplay1()
        else:
            return 0


    # dictionary for scoring each line
    scoredict = {
        "1111" : 10000,  "2222" : -10000,
        
        "1110" : 100,   "2220" : -100,
        "1101" : 100,   "2202" : -100,
        "1011" : 100,   "2022" : -100,
        "0111" : 100,   "0222" : -100,
        
        "1100" : 10,    "2200" : -10,
        "1010" : 10,    "2020" : -10,
        "1001" : 10,    "2002" : -10,
        "0101" : 10,    "0202" : -10,
        "0110" : 10,    "0220" : -10,
        "0011" : 10,    "0022" : -10,
        
        "1000" : 1,     "2000" : -1,
        "0100" : 1,     "0200" : -1,
        "0010" : 1,     "0020" : -1,
        "0001" : 1,     "0002" : -1,
        }

# -------------------------------------------------------
        
# check to see if human input is valid for current board
def ishumaninputvalid(board,humaninput):
    if board.isgameover == False:
        if humaninput in board.availablecols:
            return True
    else:
        return False

# human choice with pygame
def humanturn(board,validhumaninput):
    rownumber = board.finddrop(validhumaninput) 
    board.makemove(validhumaninput,rownumber)
    print "human  - " + str(validhumaninput) + ". boardscore: " + str(-board.boardscore)
    
#----------------------
  
# computer choice using maximin (random for the first spot)
def computerturn(board, depth):
    if board.turnnumber == 1:
        colpick = random.sample([2,3,4],1)[0]
        printstring1 = "comp r - " + str(colpick)
        printstring2 = "."
    else:
        colpick,minimaxscore = minimaxab(board,depth,-100000,100000)
        if len(colpick)==0:
            colpick = board.availablecols[0]
        else:
            colpick = colpick[-1]
        printstring1 = "comp m - " + str(colpick)
        printstring2 = ". maximinscore: " + str(minimaxscore)
    rownumber = board.finddrop(colpick)
    board.makemove(colpick, rownumber)
    print printstring1 + ". boardscore: " + str(-board.boardscore) + printstring2
    

#---------------------

def minimaxab(board,depth,alpha,beta):

    playersymbol = board.currentplayer
    movesequence = []  # create list to record move sequence
    availablemoves = board.availablesqs

    # check to see if game over (there is a winner)
    if board.winner != 0:
        if board.winner == playersymbol:
            return (movesequence,10000)
        else:
            return (movesequence,-10000)
    # check to see if game over (no more moves - draw)
    elif len(availablemoves) == 0:
        return (movesequence,0)
    # check if depth has been reached
    elif depth <= 0:
        return (movesequence,board.boardscore)
    
    for [colmove,rowmove] in availablemoves:
        # for all moves create new board and assign relevant symbol
        newboard = copy.deepcopy(board)
        newboard.makemove(colmove,rowmove)
        newalpha = -beta
        newbeta = -alpha
        
        # minimax on the newboard
        (newmovesequence, newboardvalue) = minimaxab(newboard,depth-1,newalpha,newbeta)
        newboardvalue = -newboardvalue   # switch score between players

        if newboardvalue >= beta:
            return (movesequence,newboardvalue)
        if newboardvalue > alpha:
            alpha = newboardvalue
            movesequence = newmovesequence
            movesequence.append(colmove)

    return (movesequence, alpha)

#------------------    
## DEBUGGING FUCTIONS
##
##def minimaxdebug(board,depth,playersymbol,symbol):
##    print "\n\nrun minimax, dpth=%d, plrsym=%d, sym=%d" %(depth,playersymbol,symbol)##
##    printbd(board)##
##    # create list to record move sequence
##    movesequence=[]
##    print movesequence
##    
##    # create a list of available moves (empty squares [i,j] on board)
##    availablemoves=availablesquares(board)
##    
##
##    # check to see if game over (there is a winner)
##    if winner(board)!=0:
##        print "winner found"##
##        if winner(board)==playersymbol:
##            print (movesequence,100000)##
##            return (movesequence,100000)
##        else:
##            print (movesequence,-100000)##
##            return (movesequence,-100000)
##    # check to see if game over (no more moves - draw)
##    elif len(availablemoves)==0:
##        return (movesequence,0)
##    # check if depth has been reached
##    elif depth<=0:
##        print "depth reached"##
##        print (movesequence,boardscore(board,playersymbol))##
##        return (movesequence,boardscore(board,playersymbol))
##
##    # are we checking for computer's turn or opponent's turn (max or min)
##    if playersymbol==symbol:
##        newbestscore = lambda x,y: x<y   #maximise moves
##        bestscore = -100000
##        print "maximising.."##
##    else:
##        newbestscore = lambda x,y: x>y   #minimise moves
##        bestscore = 100000
##        print "minimising.."##
##    
##    for [colmove,rowmove] in availablemoves:
##        print "trying: col %d, row %d" %(colmove,rowmove)##
##        # for all moves create new board and assign relevant symbol
##        newboard=copy.deepcopy(board)
##        if symbol==1:
##            newboard[colmove][rowmove].assignyellow()
##            newsymbol=2
##        else:    # if symbol==2
##            newboard[colmove][rowmove].assignred()
##            newsymbol=1
##        
##        # minimax on the newboard
##        (newmovesequence, newboardvalue) = minimax(newboard,depth-1,playersymbol,newsymbol)
##        print "(newmovesequence, newboardvalue)="##
##        print newmovesequence, newboardvalue##
##
##        if newbestscore(bestscore,newboardvalue)==True:
##            print "updating best score"##
##            print bestscore,newboardvalue
##            bestscore = newboardvalue
##            movesequence = newmovesequence
##            movesequence.append(colmove)
##    print "returning (end of function)"##
##    print (movesequence, bestscore)##
##    return (movesequence, bestscore)
##
###------
##
##def prsq(board,i,j):
##    return str(board[i][j].contents) + " "
##   
##def printbd(board):
##    b=board
##    for i in range(0,6):
##        print prsq(b,0,i)+prsq(b,1,i)+prsq(b,2,i)+prsq(b,3,i)+prsq(b,4,i)+prsq(b,5,i)+prsq(b,6,i)
##
