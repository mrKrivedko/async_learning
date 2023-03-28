import asyncio
import aiohttp
from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    """Отправка веб-запроса с помощью aiohttp."""
    async with aiohttp.ClientSession() as session:
        url = 'https://ya.ru'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
