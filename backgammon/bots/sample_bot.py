from .move_search_utils import search_possible_moves
from .bot import Bot

class SampleBot(Bot):
    def __init__(self, player_color):
        self.player = player_color

    def make_move(self, board, dice_results):
        board.set_player_perspective(self.player)
        result_moves = []
        new_move_added = True

        while new_move_added:

            new_move_added = False
            for i in range(len(dice_results)):
                some_moves = search_possible_moves(board, self.player,
                        dice_results[i])
                if len(some_moves) > 0:
                    some_move = some_moves[0]
                else:
                    continue

                if some_move == (-1):
                    board.remove_checker_from_bar()
                    board.push_player_checker(dice_results[i])
                    result_moves += [(self.player, some_move, dice_results[i])]
                else:
                    if some_move + dice_results[i] >= 24:
                        board.pop_player_checker(some_move)
                    else:
                        board.move_checker(some_move + dice_results[i], some_move)
                    result_moves += [(self.player, some_move, dice_results[i])]

                dice_results.remove(dice_results[i])
                new_move_added = True
                break

        return result_moves
                


