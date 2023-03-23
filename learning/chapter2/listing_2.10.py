import asyncio

from util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print('ждем и печатаем...')


async def main():
    """
    Выполнение кода, пока другие операции работают в фоне.
    """
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main=main())
