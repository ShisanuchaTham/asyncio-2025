import time
from datetime import timedelta
import asyncio

speed = 10
judit_time = 5 / speed  # seconds
opponent_time = 55 / speed  # seconds
opponents = 4
move_pairs = 30

async def game(x):
    board_time_start = time.perf_counter()
    for i in range(move_pairs):
        print(f"BOARD{x+1}-{i}  judit's made a move within {int(judit_time*speed)}")
        time.sleep(judit_time)
        print(f"BOARD{x+1}-{i}  opponent's made a move within {int(opponent_time*speed)}")
        await asyncio.sleep(opponent_time)
    print(f"BOARD{x+1} > Finished move in {(round(time.perf_counter() - board_time_start)*speed):.2f} seconds")
    return round((time.perf_counter() - board_time_start) * speed, 2)

async def main():
    board_time = 0
    time_start = time.perf_counter()
    tasks = [asyncio.create_task(game(i)) for i in range(opponents)]
    results = await asyncio.gather(*tasks)
    board_time = sum(results)
    print(f"Total time taken: {timedelta(seconds=round(board_time))}")
    print(f"All games finished in {board_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())