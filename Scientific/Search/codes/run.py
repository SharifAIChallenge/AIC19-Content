from search import search
from driver import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('board')
    args = parser.parse_args()

    read(args.board)

    start = timeit.default_timer()

    frontier = search(initial_state)

    stop = timeit.default_timer()
		
    export(frontier, stop-start)


function_map = {
    'bfs': bfs,
    'dfs': dfs,
    'ast': ast,
    'ida': ida
}

if __name__ == '__main__':
    main()
