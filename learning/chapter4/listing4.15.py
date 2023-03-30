import asyncio
import aiohttp

from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    """Использование таймаутов в  wait."""
    async with aiohttp.ClientSession() as session:
        URL = 'https://ya.ru'
        fetchers = [
            asyncio.create_task(fetch_status(session, URL)),
            asyncio.create_task(fetch_status(session, URL)),
            asyncio.create_task(fetch_status(session, URL, delay=3))
        ]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'Количество завершившихся задач: {len(done)}')
        print(f'Количество ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
