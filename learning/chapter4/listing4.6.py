import asyncio
import aiohttp

from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    """Конкурентное выполнение запросов с помощью gather."""
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        # генерируем список сопрограмм для каждого запроса,
        # который мы хотим отправить
        requests = [fetch_status(session, url) for url in urls]
        # ждем завершения всех запросов (~6 с.)
        status_codes = await asyncio.gather(*requests)

        # синхронное выполнение 1000 запросов (~231 с.)
        # status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)

# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
