import asyncio

from util import async_timed


@async_timed()
async def main():
    """Создание цикла событий вручную."""
    await asyncio.sleep(1)
    print('Проснулись!')


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
