from supervisor import Supervisor
from bots.sample_bot import SampleBot
from bots.aggressive_bot import AggressiveBot
import logging
import datetime


def main():
    match_results = {
            'W' : 0,
            'B' : 0
            }

    for i in range(1000):
        game_supervisor = Supervisor(AggressiveBot('B'), SampleBot('W'),
                            datetime.datetime.now())
        match_results[game_supervisor.play_game()] += 1

    print(match_results)




if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG) # DEBUG for development,
                                             # ERROR for benchmarks
    main()



