from .move_search_utils import search_possible_moves
from .bot import Bot

class SampleBot(Bot):
    def __init__(self, player_color):
        self.player = player_color

    def make_move(self, board, dice_results):
        board.set_player_perspective(self.player)
        result_moves = []
        for dice_result in dice_results:
            some_moves = search_possible_moves(board, self.player,
                    dice_result)
            if len(some_moves) > 0:
                some_move = some_moves[0]
            else:
                continue

            if some_move == (-1):
                board.remove_checker_from_bar()
                board.push_player_checker(dice_result)
                result_moves += [(self.player, some_move, dice_result)]
            else:
                if some_move + dice_result >= 24:
                    board.pop_player_checker(some_move)
                else:
                    board.move_checker(some_move + dice_result, some_move)
                result_moves += [(self.player, some_move, dice_result)]

        return result_moves
                


