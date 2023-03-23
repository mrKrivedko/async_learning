import asyncio

from util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter


@async_timed()
async def main():
    """Попытка конкурентного выполнения счетного кода."""
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())

    await task_one
    await task_two


asyncio.run(main())
