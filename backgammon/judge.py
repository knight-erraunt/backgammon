


class Judge():
    """ A class which contains methods for checking and executing game
    logic. Should probably not be instantiated. """

    # TODO: big ugly code with little abstraction, good candidate
    # for future refactor

    # UNTESTED, doubtfully working correctly

    @staticmethod
    def _validate_move(move):
        " Just a rough validation for the move, never to much caution. "

        assert len(move) == 3

        player, spike_index, fields_to_move = move

        assert player in ['W', 'B']
        assert spike_index in range(-1, 24)
        assert fields_to_move in range(1, 7)

        return (player, spike_index, fields_to_move)

    @staticmethod
    def _put_checker_to_spike(board, spike_index, check_color):
        if board.spikes[spike_index] == 0:
            board.spikes[spike_index] = (1, check_color)
        elif board.spikes[spike_index][1] == check_color:
            board.spikes[spike_index][0] += 1
        else:
            board.spikes[spike_index] = (1, check_color)
            board.bar[[x for x in ['B', 'W'] if x != check_color][0]] += 1

    @staticmethod
    def check_move(board, move):
        """ Method taking a board state and a move and returning wether the
        move is a valid move. move is of the form 
        ('W'|'B', (-1)-23, 1-6). """

        player, spike_index, fields_to_move = Judge._validate_move(move)

        # 1. moving out of the bar
        # 2. check if all are at home
        # 3. check if the source is of the valid player
        # 4. check if the destination is valid

        # 1.
        if spike_index == (-1):
            if player == 'W' and board.bar['W'] != 0:
                if board.spikes[24 - fields_to_move] == 0 or
                        board.spikes[24 - fields_to_move][1] == 'W':
                    return True
                else:
                    return False
            elif player == 'B' and board.bar['B'] != 0:
                if board.spikes[fields_to_move - 1] == 0 or
                        board.spikes[fields_to_move - 1][1] == 'B':
                    return True
                else:
                    return False
            else:
                return False

        # 2.
        all_at_home = True
        if player == 'W':
            for i in range(0, 18):
                if board.spikes[i] != 0 and board.spikes[i][1] == 'W':
                    all_at_home = False
        else:
            for i in range(6, 24):
                if board.spikes[i] != 0 and board.spikes[i][1] == 'B':
                    all_at_home = False

        # 3.
        if board.spikes[spike_index] == 0 or
           board.spikes[spike_index][1] != player:
            return False

        # 4.
        dest_spike_index = spike_index
        if player == 'W':
            dest_spike_index += fields_to_move
        else:
            dest_spike_index -= fields_to_move

        if dest_spike_index < 0 or dest_spike_index > 23:
            return all_at_home

        if board.spikes[dest_spike_index] == 0 or
           board.spikes[dest_spike_index][1] == player or
           board.spikes[dest_spike_index][0] == 1:
               return True
        else:
            return False
    
    @staticmethod
    def execute_move(board, move):
        """ Executes the move on the board and returns the board
        assumes the move has been previously checked by the check_move
        function. """

        player, spike_index, fields_to_move = Judge._validate_move(move)

        # 1. remove from the bar if the move demands it
        # 2. remove one checker from the source place
        # 3. check if dest is out of board
        # 4. else add checker to dest, possibly removing the oponents
        #                                                       checker
        
        if spike_index != (-1):
            dest_spike_index = spike_index
            if player == 'W':
                dest_spike_index += fields_to_move
            else:
                dest_spike_index -= fields_to_move
        else:
            if player == 'W':
                dest_spike_index = 24 - fields_to_move
            else:
                dest_spike_index = fields_to_move - 1

        # 1.
        if spike_index == (-1):

            board.bar[player] -= 1

            if player == 'W':
                Judge._put_checker_to_spike(board, dest_spike_index, 'W')
            else:
                Judge._put_checker_to_spike(board, dest_spike_index, 'B')
                
            return board

        # 2.
        if board.spikes[spike_index][0] == 1:
            board.spikes[spike_index] = 0
        else:
            board.spikes[spike_index][0] -= 1

        # 3.
        if dest_spike_index < 0 or dest_spike_index > 23:
            return board
        
        # 4.
        if player == 'W':
            Judge._put_checker_to_spike(board, dest_spike_index, 'W')
        else:
            Judge._put_checker_to_spike(board, dest_spike_index, 'B')
            
        return board


