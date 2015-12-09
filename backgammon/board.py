

class Board():
    """ A class for the sole purpose of holding information about the
    board state. This class is used to communicate the board state
    between the game server, judge and clients. """

    def __init__(self):
        " Creates a board without any prior moves executed. "

        " Board is represented by a line of field beginning at the top
        right and ending in the bottom right going all around. Stack of
        checkers is represented by a pair (amount, color). "
        self.spikes = 
            [(2, 'W'), 0, 0, 0, 0, (5, 'B'),
                    0, (3, 'B'), 0, 0, 0, (5, 'W'),
             (5, 'B'), 0, 0, 0, (3, 'W'), 0,
                    (5, 'W'), 0, 0, 0, 0, (2, 'B')]
        self.bar {
                'W' : 0,
                'B' : 0
                }



