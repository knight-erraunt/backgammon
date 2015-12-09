from copy import deepcopy
import logging
from board import Board
from judge import Judge
from random import randint

log = logging.getLogger("Game")

class Supervisor():
    """ Class responsible for supervising the game and logging the
    results. """

    def __init__(self, black_player, white_player):
        self.players = {
                'W' : white_player,
                'B' : black_player
                }
        self.board = Board()

    def double_dice(self):
        """ Returns the result of a double dice roll, doubles the amount
        of dices if the dices have the same results (look backgammon
        rules """
        a, b = randint(1, 6), randint(1, 6)
        if a == b:
            return [a, b, a, b]
        else:
            return [a, b]
        
    def play_game(self):
        log.info("Game started")
        
        current_player, prev_player = 'W', 'B'

        while Judge.return_winner(self.board) == None:
            log.info(current_player + ' players turn')
            dice_results = self.double_dice()
            log.info("Dice results : " + str(dice_results))

            if not Judge.has_possible_moves(self.board, current_player,
                    dice_results):
                log.info("no possible moves with this dice results, " \
                    "skipping player")
                current_player, prev_player = prev_player, current_player
                continue

            board_copy = deepcopy(self.board)
            moves = self.players[current_player].make_move(board_copy,
                    dice_results)
            
            log.info("Player wants to make moves: " + str(moves))

            for move in moves:
                if Judge.check_move(self.board, move):
                    dice_results.remove(move[2])
                    Judge.execute_move(self.board, move)
                else:
                    log.error(str(move) + " is invalid")
            
            if len(dice_results) > 0 and \
                Judge.has_possible_moves(self.board,
                                        current_player,
                                        dice_results):
                    log.error("Player did not make all the possible moves")

            current_player, prev_player = prev_player, current_player
        
        winner = Judge.return_winner(self.board)
        log.info(str(winner) + " player has won")
        log.info("Game ended")


