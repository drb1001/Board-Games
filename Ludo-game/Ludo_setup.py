# http://en.wikipedia.org/wiki/Ludo_(board_game)

# approach:

# class board = dictionary of where each piece is (since the board doesn't change)
# 16 pieces (include if not all 4 players are playing - they are always home)
#   - 1-4 player one, 5=8 player 2 etc
# a number showing progress from that players perspective :
#   0 = yard, 1 just out of the yard,
#   11 is next player's '1',  21 is next player's yard, 31 is next players yard
#   40 is on edge of home straight,
#   41-44 are home squares,  45 is finish



# class space

# class player


# move function should be something like:
# call when it is your turn
# take board state + dice roll as input
# output an array (len = 4) in the order of preference of piece number
# eg: [3,2,4,1] means try moving piece 3, if that doesn't work, move piece 2 .. etc)

# if this is invalid - the board handles the error and asks for another resonse
# 3 invalid response in a row and you forfeit :)
# time > 100 secondss => error


## RULES:

# 2-4 players
# 4 yard squares
# 4 men each
# roll 1 dice ( 6 is another go)
# given a dice roll and a playing piece - you can make the move
# land on top means other dude goes back home
# 6 to exit home
#

# Step 1 player vs really simple computer