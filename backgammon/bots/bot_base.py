from .move_search_utils import search_possible_moves
from .bot import Bot
from copy import deepcopy
from itertools import product

class BotBase(Bot):
    def __init__(self, player_color):
        self.player = player_color

        self.init_parameters()

    def init_parameters(self):
        self.depth = 1
        self.evaluation_functions = [(1, self.sum_dist)]

    def sum_dist(self, board, player):
        """ Sample evauluation function, the parameters are
        always the same. The function should return a value
        between 0 and 1 inclusively. 
        1 - position good for player
        0 - position bad for player """

        board.set_player_perspective(player)
        result = 0
        worst_dist_sum = 24 * 15

        for i in range(len(board.spikes)):
            if board.spikes[i][0] != 0 and \
                    board.spikes[i][1] == player:
                result += (24 - i) * board.spikes[i][0]
        
        return 1 - result / worst_dist_sum

    @staticmethod
    def opponent(player):
        opponents = {
                'W' : 'B',
                'B' : 'W'
                }
        return opponents[player]

    def board_value(self, board, player):
        weight_sum = sum([ev_fn[0] for ev_fn in
            self.evaluation_functions])
        return sum([fn[1](board, player) * fn[0] / weight_sum for fn in
            self.evaluation_functions]) 

    def relative_board_value(self, board, player):
        # higher better
        return self.board_value(board, player) / \
                self.board_value(board, BotBase.opponent(player))

    def make_moves(self, board, dice_results):
        moves_choosen = self.choose_moves(board, self.player,
                                dice_results, self.depth)
        # TODO use the moves info to change the bot state

        # return the actual move from (score, moves) tuple
        return moves_choosen[1]

    def exec_move(self, board, move):
        if move[1] != None:
            if move[1] == (-1):
                board.remove_checker_from_bar()
                board.push_player_checker(move[2] - 1)
            elif move[1] + move[2] < 24:
                board.move_checker(move[1] + move[2], move[1])
            else:
                board.pop_player_checker(move[1])
            return [move]
        else:
            return []


    def choose_moves(self, board, player, dice_results, depth):
        result_moves = []
        result_score = 0

        if len(dice_results) > 2:
            # dices are the same - don't care about the order
            board_copy = deepcopy(board)
            board_copy.set_player_perspective(player)

            for _ in range(4):
                move = self.choose_move(board_copy, player, dice_results[0], depth)
                result_moves += self.exec_move(board_copy, move)
            result_score = self.relative_board_value(board_copy, player)

        else:
            board_one, board_two = deepcopy(board), deepcopy(board)
            board_one_moves, board_two_moves = [], []
            board_one.set_player_perspective(player)
            board_two.set_player_perspective(player)
        
            move = self.choose_move(board_one, player, dice_results[0], depth)
            board_one_moves += self.exec_move(board_one, move)

            move = self.choose_move(board_one, player, dice_results[1], depth)
            board_one_moves += self.exec_move(board_one, move)

            # dices used in the reversed order
            move = self.choose_move(board_two, player, dice_results[1], depth)
            board_two_moves += self.exec_move(board_two, move)

            move = self.choose_move(board_two, player, dice_results[0], depth)
            board_two_moves += self.exec_move(board_two, move)

            board_one_val = self.relative_board_value(board_one, player)
            board_two_val = self.relative_board_value(board_two, player)
            if board_one_val > board_two_val:
                result_moves = board_one_moves
                result_score = board_one_val
            else:
                result_moves = board_two_moves
                result_score = board_two_val

        return (result_score, result_moves)

    def all_possible_dice_rolls(self):
        # TODO
        # should not be generated each time
        all_pairs = list(product(range(1,7), repeat=2))
        all_pairs = map(list, all_pairs)
        all_pairs = list(all_pairs)
        for i in range(len(all_pairs)):
            if all_pairs[i][0] == all_pairs[i][1]:
                all_pairs[i] = all_pairs[i] + all_pairs[i]
        return all_pairs

    def choose_move(self, board, player, dice_result, depth):
        possible_moves = search_possible_moves(board, player,
                dice_result)

        best_move, best_move_score = None, 0

        for possible_move in possible_moves:
            tmp_board = deepcopy(board)
            if possible_move == (-1):
                tmp_board.remove_checker_from_bar()
                tmp_board.push_player_checker(dice_result - 1)
            elif possible_move + dice_result < 24:
                tmp_board.move_checker(possible_move + dice_result,
                        possible_move)
            else:
                tmp_board.pop_player_checker(possible_move)

            if depth > 0:
                all_possibilities = self.all_possible_dice_rolls()
                for dice_roll in all_possibilities:
                    result, _ = self.choose_moves(tmp_board,
                            BotBase.opponent(player), dice_roll, depth-1)
                    if result > best_move_score:
                        best_move_score = result
                        best_move = possible_move
            else:
                result = self.relative_board_value(tmp_board, player)
                if result > best_move_score:
                    best_move_score = result
                    best_move = possible_move

        return (player, best_move, dice_result)



