import asyncio
from asyncio import CancelledError

from util import delay


async def main():
    """Снятие задачи."""
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Задача не закончилась, проверим через секунду снова.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            # Вызов cancel не прерывает задачу, он снимает её,
            # только если она уже находится в точке ожидания
            # или когда дойдет до следующей точки.
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('Наша задача была снята.')


asyncio.run(main())
