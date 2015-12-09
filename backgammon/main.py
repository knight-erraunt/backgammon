from supervisor import Supervisor
from bots.sample_bot import SampleBot
import logging


def main():
    match_results = {
            'W' : 0,
            'B' : 0
            }

    for i in range(1000):
        game_supervisor = Supervisor(SampleBot('B'), SampleBot('W'), i)
        match_results[game_supervisor.play_game()] += 1

    print(match_results)




if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR) # DEBUG for development,
                                             # ERROR for benchmarks
    main()



