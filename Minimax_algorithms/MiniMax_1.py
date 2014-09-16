####################
# General form of MiniMax algorithm
#
# functions needed:
# emptysquares(board)
# gameover(board)
# winner(board)
# boardscore(board)
# makemove(board,move,symbol)
# newsymbol(symbol)

##----------------------

import copy

#---------------------

def minimax(board,depth,playersymbol,symbol):

    # create list to record move sequence
    movesequence=[]
    
    # create a list of available moves (empty squares on board)
    availablemoves=emptysquares(board)

    # check to see if game over (there is a winner / draw) and return score
    if gameover(board):
        if winner(board)==playersymbol:
            return (movesequence,100)       # 100 is best case scenario (win) - may need to increase if heuristic is used 
        elif winner(board)==opponentsymbol:
            return (movesequence,-100)
        elif winner(board)==drawsymbol or len(availablemoves)==0:
            return (movesequence,0)
        elif depth<=0:
            return (movesequence, boardscore(board))

    # are we checking for computer's turn or opponent's turn (max or min)
    if playersymbol==symbol:
        maxminoperator=1
    else:
        maxminoperator=-1
    def isnewscorebetter(oldscore,newscore):
        return (oldscore*maxminoperator)<(newscore*maxminoperator)
    bestscore=100*maxminoperator

    # for all available moves create new board and updates for move
    for move in availablemoves:
        newboard=copy.deepcopy(board)
        makemove(newboard,move,symbol)
        
        # minimax on the newboard
        (newmovesequence, newboardvalue) = minimax(newboard,depth-1,playersymbol,newsymbol(symbol))

        # once minimax has been full depth, check if sequence results in a better score
        if isscorebetter(bestscore,newboardvalue):
            bestscore = newboardvalue
            movesequence = newmovesequence
            movesequence.append(move)

    return (movesequence, bestscore)

#----------------------


def minimaxMin(board,depth):
    if depth <= 0:
      #-- positive values are good for the maximizing player
      #-- negative values are good for the minimizing player
      return boardscore(node)
   
   #-- maximizing player is (+1)
   #-- minimizing player is (-1)
    if currentplayer==1:
        alpha=10000
    else:
        alpha=10000
 
   newboard=copy.deepcopy(board)

   while newboard!=nil #???
      newscore = minimax(child,depth-1)
      alpha = node.player==1 and math.max(alpha,score) or math.min(alpha,score)
      newboard = next_child(node,child)
   return alpha


#--------------------------

def minimaxMax(board,depth):

    movesequence=[]
    
    if isgameover(board):
        return (movesequence, boardscore(board))
    elif depth<=0:
        return (movesequence, boardscore(board))

    availablemoves=emptysquares(board)
    bestscore = -100   # start with worst case scenario
    
    for move in availablemove:
        newboard=copy.deepcopy(board)
        makemove(newboard,move,symbol)
        
        (newmovesequence, newscore) = minimaxMin(child,depth-1)      
        if newscore > bestscore:
            bestscore = newscore
            movesequence = newmovesequence
            movesequence.append(move)
    return (movesequence, bestscore)


def minimaxMin(board,depth):

    movesequence=[]
    
    if isgameover(board):
        return (movesequence, boardscore(board))
    elif depth<=0:
        return (movesequence, boardscore(board))

    availablemoves=emptysquares(board)
    bestscore = 100   #start with worst case scenario for min player
    
    for move in availablemoves:
        newboard=copy.deepcopy(board)
        makemove(newboard,move,symbol)
        
        (newmovesequence, newscore) = minimaxMax(child,depth-1)
        if newscore < bestscore:
            bestscore = newscore
            movesequence = newmovesequence
            movesequence.append(move)
    return (movesequence, bestscore) 


#-----------------------------


def minimaxscores(board,depth):
    
    if depth<=0 or isgameover(board): 
        return boardscore(board)

    availablemoves=emptysquares(board)
    bestscore = -100   #start with worst case scenario for min player
    
    for move in availablemoves:
        newboard=copy.deepcopy(board)
        makemove(newboard,move,symbol)
        
        bestscore = max(bestscore, -minimaxMax(newboard,depth-1) )

    return bestscore 


def maxmin(board,depth):

     if depth<=0 or isgameover(board): 
        return boardscore(board)

    availablemoves=emptysquares(board)
    bestscore = -100   #start with worst case scenario for min player
    
    for move in availablemoves:
        newboard=copy.deepcopy(board)
        makemove(newboard,move,symbol)
        
        bestscore = max(bestscore, -minimaxMax(newboard,depth-1) )

    return bestscore 

