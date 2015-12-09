from copy import deepcopy
import logging
from board import Board
from judge import Judge
import random

log = logging.getLogger("Game")

class Supervisor():
    """ Class responsible for supervising the game and logging the
    results. """

    def __init__(self, black_player, white_player, random_seed):
        random.seed(random_seed)
        self.players = {
                'W' : white_player,
                'B' : black_player
                }
        self.board = Board()

    def double_dice(self):
        """ Returns the result of a double dice roll, doubles the amount
        of dices if the dices have the same results (look backgammon
        rules """
        a, b = random.randint(1, 6), random.randint(1, 6)
        if a == b:
            return [a, b, a, b]
        else:
            return [a, b]
        
    def play_game(self):
        log.info("Game started")
        
        current_player, prev_player = 'W', 'B'
        incorrect_move_attempted = False
        not_all_moves_requested = False

        while not incorrect_move_attempted and \
                Judge.return_winner(self.board) == None:
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
            dices_copy = deepcopy(dice_results)
            moves = self.players[current_player].make_move(board_copy,
                    dices_copy)
            
            log.info("Player wants to make moves: " + str(moves))

            for move in moves:
                if Judge.check_move(self.board, move):
                    dice_results.remove(move[2])
                    Judge.execute_move(self.board, move)
                else:
                    log.error(str(move) + " is invalid")
                    incorrect_move_attempted = True
                    break
            
            if Judge.has_possible_moves(self.board,
                                        current_player,
                                        dice_results):
                log.error("Player did not make all the possible moves")
                not_all_moves_requested = True
                break

            current_player, prev_player = prev_player, current_player

        if incorrect_move_attempted:
            log.error(str(prev_player) + " player has won, due to " \
                "incorrect move of the opponent")
            winner = prev_player
        elif not_all_moves_requested:
            log.error(str(prev_player) + " player has won, due to " \
                "opponent not requesting all possible moves")
            winner = prev_player
        else: 
            winner = Judge.return_winner(self.board)
            log.info(str(winner) + " player has won")
        
        log.info("Game ended")

        return winner





