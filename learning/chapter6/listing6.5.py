import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import time

from util import async_timed


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'операция с {count_to} выполнилась за {end - start} секунд.')
    return counter


@async_timed()
async def main():
    """Исполнитель пула процессов в сочетани с asyncio."""
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 100_000_000]
        # сформируем все обращения у к пулу процессов, поместив их в список
        calls: list[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))

        results = asyncio.as_completed(call_coros)

        for result in results:
            print(await result)

        # ----------

        results = await asyncio.gather(*call_coros)

        for result in results:
            print(result)


if __name__ == '__main__':
    asyncio.run(main())
