
class Board(object):
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.current_player = 0
        self.active_players = [1, 0, 1, 0]
        if num_players == 4:
            self.active_players = [1, 1, 1, 1]
        elif num_players == 3:
            self.active_players = [1, 0, 1, 1]

        self.board_state = [0] * 16

        # index: 16 pieces (include if not all 4 players are playing).  pieces 0-3 are player 0, 4-7 are player 1 etc
        # value: a number showing progress from that players perspective
        #      0 = yard
        #      1 = just out of the yard
        #      11 = next player's '1'
        #      21 = next player's '1'
        #      31 = next players '1'
        #      40 = on edge of home straight
        #      41-44 are home squares,
        #      45+ = finished (home)
        # always from player 1's perspective

    def set_next_player(self):
        self.current_player = (self.current_player + 1) % 4
        if self.active_players[self.current_player] == 0:
            self.set_next_player()

    def is_game_over(self):
        for i in range(0, 4):
            if self.board_state[i] >= 45 and self.board_state[i+1] >= 45 \
                    and self.board_state[i+2] >= 45 and self.board_state[i+3] >= 45:
                return True
        return False

    def is_valid_move(self, piece, dice_roll):
        ref_piece = 4 * self.current_player + piece
        if self.board_state[ref_piece] == 0:
            if dice_roll < 6:
                return False
            elif dice_roll == 6:
                for each_piece in self.board_state:
                    if each_piece == 1:   # TBD: if piece is my own, and is in spot 1
                        return False
        elif self.board_state[ref_piece] + dice_roll < 45 and "piece at new position is own piece":
            return False

        else:
            return True

    def exists_valid_move(self, dice_roll):
        for check_piece in range(0, 4):
            if self.is_valid_move(check_piece, dice_roll):
                return True
        return False

    def get_position(self, player, piece):
        return False

    def update_board(self, piece, dice_roll):
        self.board_state[piece] += dice_roll
        for each_piece in self.board_state:
            if self.board_state[each_piece] == self.board_state[piece]:
                self.board_state[each_piece] = 0
