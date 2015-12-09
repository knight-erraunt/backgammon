

def search_possible_moves(board, player, on_dice):
    """ Returns the possible moves with on_dice one dice roll result
    and current board state. The moves are returned as a list of
    spikes from which we can choose to move. """

    board.set_player_perspective(player) 

    if board.bar[player] > 0:
        if board.valid_dest(on_dice - 1):
            return [-1]
        else:
            return []

    if board.all_at_home():
        return [x for x in board.player_spikes() if x + on_dice >= 24 or
                board.valid_dest(x + on_dice)]
    else:
        return [x for x in board.player_spikes() if x + on_dice < 24 and
                board.valid_dest(x + on_dice)]
    




