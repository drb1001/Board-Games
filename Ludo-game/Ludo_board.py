import random



def roll_dice():
    return random.randint(1,6)

def is_valid_move(board, player, piece, diceroll):
    return False
    # if piece is in yard and diceroll < 6 then return false
    # if piece is in yard and diceroll = 6 and new position is own piece then false
    # if piece is not in open and new position is own piece then false
    # else true

def make_move(board, current_player, piece, dice_roll):
    return True

def is_game_over(board):
    return False
    # for each player
    # are all pieces home? if yes true
    # else false

def is_valid_choice(choice):
    # is it an array, is it size 4, does it contains 0-4
    return True

def exists_valid_move(board, current_player, dice_roll):
    for piece in range(0,4):
        if is_valid_move(board, current_player, piece, dice_roll):
           return True
    return False



# initialise board + pieces + players (randomly assign player starting point and order)
board = []
current_player = 0
active_players = [1,0,1,0]


while True:

    dice_roll = roll_dice()
    if exists_valid_move(board, current_player, dice_roll):
        choice = get_move_choice()
        if is_valid_choice(choice):
            for piece in choice:
                if is_valid_move(board, current_player, piece, dice_roll):
                    make_move(board, current_player, piece, dice_roll)
                    break

            if is_game_over(board):
                break
            else:
                if dice_roll != 6:
                    current_player = (current_player + 1) % 4

        else: current_player = (current_player + 1) % 4
    else: current_player = (current_player + 1) % 4

# need to check next player is playing


# maybe write a log system per turn / per match - or some game logging statistics summary numbers


