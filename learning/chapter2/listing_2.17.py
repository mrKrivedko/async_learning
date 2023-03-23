import asyncio

from util import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'Засыпаю на {delay_seconds}с.')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds}с закончился.')
    return delay_seconds


@async_timed()
async def main():
    """Хронометраж двух конкурентных задач с помощбю декоратора."""
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(5))

    await task_one
    await task_two


asyncio.run(main())
