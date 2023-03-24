import asyncio

from util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for _ in range(100_000_000):
        counter += 1
    return counter


@async_timed()
async def main() -> None:
    """Выполнение счетного кода в отладочном режиме."""
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


asyncio.run(main(), debug=True)
