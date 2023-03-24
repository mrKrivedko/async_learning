import asyncio
import time

from util import async_timed, delay


def call_later():
    print('Меня вызовут в ближайшем будущем!')
    time.sleep(5)
    print('5sec later')


@async_timed()
async def main():
    """Получение доступа к циклу событий."""
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
