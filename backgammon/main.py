from supervisor import Supervisor
from bots.sample_bot import SampleBot
import logging


def main():
    logging.basicConfig(level=logging.DEBUG)

    game_supervisor = Supervisor(SampleBot('B'), SampleBot('W'))

    game_supervisor.play_game()




if __name__ == '__main__':
    main()



