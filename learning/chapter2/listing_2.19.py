import asyncio

from util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter


@async_timed()
async def main():
    """Счетный код и длительная задача."""
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(5))

    await task_one
    await task_two
    await delay_task


# Если требуется выполнить счетную работу и всё-таки использовать async/await,
# то это можно сделать. Но придется воспользоваться многопроцессностью
# и выполнять задачи в пуле процессов (см. главу 6)
asyncio.run(main())
