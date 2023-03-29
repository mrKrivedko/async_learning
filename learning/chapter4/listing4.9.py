import asyncio
import aiohttp

from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    """Задание таймаута для as_completed."""
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://ya.ru', 1),
            fetch_status(session, 'https://ya.ru', 10),
            fetch_status(session, 'https://ya.ru', 10)
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел таймаут')

        for task in asyncio.tasks.all_tasks():
            print(task)


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
