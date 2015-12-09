from .move_search_utils import search_possible_moves
from .bot import Bot

class SampleBot(Bot):
    def __init__(self, player_color):
        self.player = player_color

    def make_any_move(self, board, dice_results, result_moves):
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
                    board.pop_player_checker(first_move)
                else:
                    board.move_checker(first_move + dice_results[i],
                                                            first_move)
                
            result_moves += [(self.player, first_move, dice_results[i])]
            dice_results.remove(dice_results[i])
            return True
        return False

    def make_moves(self, board, dice_results):
        board.set_player_perspective(self.player)
        result_moves = []

        while self.make_any_move(board, dice_results, result_moves):
            pass

        return result_moves
                


