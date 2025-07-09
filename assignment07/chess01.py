import time
from datetime import timedelta

speed = 100
judit_time = 5/speed # seconds
opponent_time = 55/speed # seconds
opponents = 1
move_pairs = 30

def game(x):
    board_time_start = time.perf_counter()
    for i in range(move_pairs):
        print(f"BOARD{x+1}-{i}  judit's made a move within {int(judit_time*speed)}")
        time.sleep(judit_time)
        print(f"BOARD{x+1}-{i}  opponent's made a move within {int(opponent_time*speed)}")
        time.sleep(opponent_time)
    print(f"BOARD{x+1} > Finished move in {(round(time.perf_counter())-board_time_start)*speed:.2f} seconds")
    return round(time.perf_counter() - board_time_start)*speed

if __name__ == "__main__":
    board_time = 0
    time_start = time.perf_counter()
    for i in range(opponents):
        board_time += game(i)
    print(f"Total time taken: {timedelta(seconds=round(board_time))}")
    # print(f"Total time taken: {timedelta(seconds=round(time.perf_counter() - time_start))}")
    print(f"All games finished in {board_time} seconds")