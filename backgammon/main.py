from supervisor import Supervisor
from bots.sample_bot import SampleBot
from bots.aggressive_bot import AggressiveBot
from bots.bot_base import BotBase
import logging
import datetime


def main():
    match_results = {
            'W' : 0,
            'B' : 0
            }

    for i in range(100):
        game_supervisor = Supervisor(BotBase('B'), SampleBot('W'),
                            datetime.datetime.now())
        match_results[game_supervisor.play_game()] += 1

    print(match_results)




if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG) # DEBUG for development,
                                             # ERROR for benchmarks
    main()



