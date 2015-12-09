


class MoveSearchUtils():
    """ A class containing utils to search for moves, may be used by
    the judge/supervisor or the bots. """

    def search_possible_moves(board, player, on_dice):
        """ Returns the possible moves with on_dice one dice roll result
        and current board state. The moves are returned as a list of
        spikes from which we can choose to move. """

        if board.bar[player] > 0:
            if player == 'W':
                if board.spikes[24 - on_dice] == 0 or
                   board.spikes[24 - on_dice][1] == 'W' or
                   board.spikes[24 - on_dice][0] == 1:
                       return [-1]
                else:
                    return []
            else:
                if board.spikes[on_dice - 1] == 0 or
                   board.spikes[on_dice - 1][1] == 'B' or
                   board.spikes[on_dice - 1][0] == 1:
                       return [1]
                else:
                    return [] 

        # ugly copy & paste from the Judge class, definitely to be refactored
        all_at_home = True
        if player == 'W':
            for i in range(0, 18):
                if board.spikes[i] != 0 and board.spikes[i][1] == 'W':
                    all_at_home = False
        else:
            for i in range(6, 24):
                if board.spikes[i] != 0 and board.spikes[i][1] == 'B':
                    all_at_home = False


        







