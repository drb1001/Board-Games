import random

# really really really simple ai -
def really_simple_ai(board_state, dice_roll):
    return [0, 1, 2, 3]

# random ai -
def simple_random_ai(board_state, dice_roll):
    a = [0, 1, 2, 3]
    random.shuffle(a)
    return a

# testing
# for i in range(1,10):
#     print really_simple_ai(0,0), simple_random_ai(0,0)