from game_config import *
from bots.move_search_utils import search_possible_moves


class Judge():
    """ A class which contains methods for checking and executing game
    logic. Should probably not be instantiated. """

    @staticmethod
    def _validate_move(move):
        " Just a rough validation for the move, never to much caution. "

        assert len(move) == 3

        player, spike_index, fields_to_move = move

        assert player in PLAYERS
        assert spike_index in range(-1, len(INITIAL_SPIKES_STATE))
        assert fields_to_move in range(MIN_DICE_RESULT, MAX_DICE_RESULT+1)

        return (player, spike_index, fields_to_move)

    @staticmethod
    def check_move(board, move):
        """ Method taking a board state and a move and returning wether the
        move is a valid move. move is of the form 
        ('W'|'B', (-1)-23, 1-6). """

        player, spike_index, fields_to_move = Judge._validate_move(move)

        # 1. moving out of the bar
        # 2. check if the source is of the valid player
        # 3. check if the destination is valid

        board.set_player_perspective(player)

        # 1.
        if spike_index == OUT_OF_BAR_SPECIAL_MOVE:
            if board.bar[player] < 1:
                return False

            if not board.valid_dest(fields_to_move):
                return False

            return True

        # 2.
        if not board.valid_source(spike_index):
            return False
        # 3.
        dest_spike_index = spike_index + fields_to_move

        if dest_spike_index >= len(INITIAL_SPIKES_STATE):
            return board.all_at_home()
    
        return board.valid_dest(dest_spike_index)

    @staticmethod
    def execute_move(board, move):
        """ Executes the move on the board and returns the board
        assumes the move has been previously checked by the check_move
        function. """

        player, spike_index, fields_to_move = Judge._validate_move(move)

        board.set_player_perspective(player)
        
        if spike_index == OUT_OF_BAR_SPECIAL_MOVE:
            dest_spike_index = fields_to_move
            board.remove_checker_from_bar()
        else:
            dest_spike_index = spike_index + fields_to_move
            board.pop_player_checker(spike_index)

        if dest_spike_index >= len(INITIAL_SPIKES_STATE):
            return board

        board.push_player_checker(dest_spike_index)

        return board

    @staticmethod
    def return_winner(board):
        for player in PLAYERS:
            board.set_player_perspective(player)
            if 0 == len(board.player_spikes()):
                return player

        return None

    @staticmethod
    def has_possible_moves(board, player, dice_results):
        for dice_result in dice_results:
            if 0 < len(search_possible_moves(board, player, dice_result)):
                return True
        return False





