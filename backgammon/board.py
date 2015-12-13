from game_config import *
from copy import deepcopy

class IllegalOperation(Exception):
    pass

class Board():
    """ A class for purpose of holding information about the board
    state. Also has simple helpers for board manipulation This class is
    used to communicate the board state between the game server, judge
    and clients. """

    def __init__(self):
        " Creates a board without any prior moves executed. "

        # Board is represented by a line of field beginning at the top
        # right and ending in the bottom right going all around. Stack of
        # checkers is represented by a pair (amount, color).
        self.spikes = deepcopy(INITIAL_SPIKES_STATE)
        self.bar = deepcopy(INITIAL_BAR)
        self._player_perspective = INITIAL_PLAYER_PERSPECTIVE
        self.home_size = HOME_SIZE

    def set_player_perspective(self, player):
        if self._player_perspective != player:
            self._player_perspective = player
            self.spikes.reverse()

    def all_at_home(self):
        " Relays on the variable _player_perspective "
        return 0 == len([1 for amount, player in
                        self.spikes[:-self.home_size] if player ==
                        self._player_perspective])

    def pop_player_checker(self, spike_index):
        if not self.valid_source(spike_index)
            raise IllegalOperation

        if self.spikes[spike_index][0] == 1:
            self.spikes[spike_index] = EMPTY_SPIKE
        else:
            self.spikes[spike_index][0] -= 1

    def push_player_checker(self, spike_index):
        if not self.valid_dest(spike_index):
            raise IllegalOperation

        if self.spikes[spike_index] == EMPTY_SPIKE:
            self.spikes[spike_index] = [1, self._player_perspective]
        elif self.spikes[spike_index][1] == self._player_perspective:
            self.spikes[spike_index][0] += 1
        else:
            self.spikes[spike_index] = [1, self._player_perspective]
            self.bar[[x for x in PLAYERS if x !=
                self._player_perspective][0]] += 1

    def move_checker(self, dest_spike, source_spike):
        self.pop_player_checker(source_spike)
        self.push_player_checker(dest_spike)
            
    def valid_dest(self, spike_index):
        return spike_index >= len(INITIAL_SPIKES_STATE) or \
            self.spikes[spike_index] == EMPTY_SPIKE or \
            self.spikes[spike_index][1] == self._player_perspective or \
            self.spikes[spike_index][0] == 1

    def valid_source(self, spike_index):
        return spike_index < len(INITIAL_SPIKES_STATE) and \
                self.spikes[spike_index] != EMPTY_SPIKE and \
                self.spikes[spike_index][1] == self._player_perspective

    def remove_checker_from_bar(self):
        if self.bar[self._player_perspective] == 0:
            raise IllegalOperation

        self.bar[self._player_perspective] -= 1

    def player_spikes(self):
        return [i for i, spike in enumerate(self.spikes) if 
                            spike[1] == self._player_perspective]
    



