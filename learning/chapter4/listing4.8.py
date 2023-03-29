import asyncio
import aiohttp

from util import async_timed
from chapter_4 import fetch_status


# async def fetch_status(
#         session: ClientSession,
#         url: str,
#         delay: int = 0
# ) -> int:
#     await asyncio.sleep(delay)
#     async with session.get(url) as result:
#         return result.status


@async_timed()
async def main():
    """Использование as_completed, по мере выполнения."""
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://ya.ru', 1),
            fetch_status(session, 'https://ya.ru', 1),
            fetch_status(session, 'https://ya.ru', 10)
        ]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
