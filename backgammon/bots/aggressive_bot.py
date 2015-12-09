from .move_search_utils import search_possible_moves
from .sample_bot import SampleBot


class AggressiveBot(SampleBot):
    """ An implementation of a bot which first tries to pawn opponents
    checkers """

    def make_aggressive_move(self, board, dice_results, result_moves):
        " Returns True if move was made, False otherwise "
        for i in range(len(dice_results)):
            possible_moves = search_possible_moves(board, self.player,
                    dice_results[i])
            if len(possible_moves) > 0:
                first_move = possible_moves[0]
            else:
                continue

            if first_move == (-1):
                board.remove_checker_from_bar()
                board.push_player_checker(dice_results[i] - 1)
            else:
                if first_move + dice_results[i] >= 24:
                    continue # going off the board is not really
                             # aggressive
                elif board.spikes[first_move + dice_results[i]][1] != self.player and \
                     board.spikes[first_move + dice_results[i]][1] != None:
                        board.move_checker(first_move + dice_results[i],
                                                                first_move)
                else:
                    continue

            result_moves += [(self.player, first_move, dice_results[i])]
            dice_results.remove(dice_results[i])
            return True
        return False

    def make_moves(self, board, dice_results):
        board.set_player_perspective(self.player)
        result_moves = []
        new_move_added = True

        while new_move_added:

            new_move_added = False

            while self.make_aggressive_move(board, dice_results, result_moves):
                new_move_added = True

            if self.make_any_move(board, dice_results, result_moves):
                new_move_added = True

        return result_moves



            



