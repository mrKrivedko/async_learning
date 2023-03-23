import asyncio

from util import delay


async def main():
    """Снятие задачи с помощью таймаута, но с защитой от снятия."""
    delay_task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Задача заняла более 5 секунд, и скоро закончится.')
        # await нужен для завершения задачи.
        result = await delay_task
        print(result)


asyncio.run(main())
