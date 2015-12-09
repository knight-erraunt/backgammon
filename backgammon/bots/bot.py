


class Bot():
    """ An interface class for the backgammon bots """

    def __init__(self, player_color):
        raise NotImplementedError

    def make_moves(self, board, dice_results):
        """ dice_results is a list of integers between 1 and 6. The
        result should be a list of moves. move is of the form 
        ('W'|'B', (-1)-23, 1-6). """
        raise NotImplementedError




