import random
from Ludo_setup import *
from Ludo_pygame import *

def roll_dice():
    return random.randint(1, 6)


def get_move_choice(the_board, dice_roll):
    ###
    ###
    ###
    return [0, 1, 2, 3]


def is_valid_response(choice):
    if type(choice.__name__ == 'list'):
            if sorted(choice) == [0, 1, 2, 3]:
                return True
    else:
        return False

# move function should be something like:
# call when it is your turn
# take board state + dice roll as input
# output an array (len = 4) in the order of preference of piece number
# eg: [3,2,0,1] means try moving piece 3, if that doesn't work, move piece 2 .. etc)

window, clock = pygamestart()
the_board = Board(2)
# which player is in which position -> mapping
# need to check next player is playing
# maybe write a log system per turn / per match - or some game logging statistics summary numbers

while True:

    dice_roll = roll_dice()
    draw_board(window, the_board)
    if the_board.exists_valid_move(dice_roll):
        choice = get_move_choice(the_board, dice_roll)
        if is_valid_response(choice):
            for try_piece in choice:
                if the_board.is_valid_move(try_piece, dice_roll):
                    the_board = the_board.update_board(try_piece, dice_roll)
                    break

            if the_board.is_game_over():
                break
            else:
                if dice_roll != 6:
                    the_board.set_next_player()

        else:
            the_board.set_next_player()
    else:
        the_board.set_next_player()
