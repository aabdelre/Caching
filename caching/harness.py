import sys
import argparse
import utilities
from memory import Memory
from cache import CyclicCache, LRUCache, RandomCache

# ANSI Colours for nice display

class bcolours:
    BLACK= '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--strategy',
                        help='Expects one of Memory (default), LRU, Cyclic or Random',
                        default="Memory")
    args = parser.parse_args()
    model = None
    # Create some memory of size 10.
    data = utilities.sample_data(size=10)
    #print(data)

    if args.strategy == "Memory":
        model = Memory(data)
    elif args.strategy == "Cyclic":
        model = CyclicCache(data)
    elif args.strategy == "LRU":
        model = LRUCache(data)
    elif args.strategy == "Random":
        model = RandomCache(data)
    else:
        print("Unknown strategy: {}".format(args.strategy))
        sys.exit(1)

    # Reads a list of integers from the command line. No error
    # checking, so non integers will bomb out.
    count = 0
    location = sys.stdin.readline().strip()
    while(location):
        count += 1
        location = int(location)
        print("{}{:03d}{},{}{:2d}{}, {}{}{}".format(bcolours.GREEN,
                                        count,
                                        bcolours.RESET,
                                        bcolours.BLUE,
                                        location,
                                        bcolours.RESET,
                                        bcolours.RED,
                                        model.lookup(location),
                                        bcolours.RESET))
        location = sys.stdin.readline().strip()
    print(f"Model: {bcolours.BLACK}{model.name()}{bcolours.RESET}")
    print(f"{bcolours.YELLOW}{count} Accesses{bcolours.RESET}")
    print(f"{bcolours.YELLOW}{model.get_memory_hit_count()} Memory Hits{bcolours.RESET}")
    print(f"{bcolours.YELLOW}{model.get_cache_hit_count()} Cache Hits{bcolours.RESET}")
