from game_config import *

class IllegalOperation(Exception):
    pass

class Board():
    """ A class for purpose of holding information about the board
    state. Also has simple helpers for board manipulation This class is
    used to communicate the board state between the game server, judge
    and clients. """

    def __init__(self):
        " Creates a board without any prior moves executed. "

        " Board is represented by a line of field beginning at the top
        right and ending in the bottom right going all around. Stack of
        checkers is represented by a pair (amount, color). "
        self.spikes = INITIAL_SPIKES_STATE
        self.bar = INITIAL_BAR
        self._player_perspective = INITIAL_PLAYER_PERSPECTIVE
        self.home_size = HOME_SIZE

    def set_player_perspective(player):
        if self.player_perspective != player:
            self.player_perspective = player
            self.spikes.reverse()

    def all_at_home():
        " Relays on the variable player_perspective "
        return 0 == len([1 for amount, player in
                        self.spikes[:-self.home_size] if player ==
                            self._player_perspective)

    def pop_player_checker(spike_index):
        if self.spikes[spike_index] == EMPTY_SPIKE or
                self.spikes[spike_index][1] != self._player_perspective:
            raise IllegalOperation

        if self.spikes[spike_index][0] == 1:
            self.spikes[spike_index] = EMPTY_SPIKE
        else:
            self.spikes[spike_index][0] -= 1

    def push_player_checker(spike_index):
        if not self.valid_dest(spike_index):
            raise IllegalOperation

        if self.spikes[spike_index] == EMPTY_SPIKE:
            self.spikes[spike_index] = (1, self._player_perspective)
        else:
            self.spikes[spike_index][0] += 1

    def move_checker(dest_spike, source_spike):
        self.pop_player_checker(source_spike)
        self.push_player_checker(dest_spike)
            
    def valid_dest(spike_index):
        return self.spikes[spike_index] == EMPTY_SPIKE or
                self.spikes[spike_index][1] == self._player_perspective
                self.spikes[spike_index][0] == 1

    def valid_source(spike_index):
        return self.spikes[spike_index] !== EMPTY_SPIKE and
                self.spikes[spike_index][1] == self._player_perspective

    def remove_checker_from_bar():
        if self.bar[self._player_perspective] == 0:
            raise IllegalOperation

        self.bar[self._player_perspective] -= 1
    



