import asyncio
import aiohttp
from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def fetch_status(
        session: ClientSession,
        url: str
) -> int:
    ten_millis = aiohttp.ClientTimeout(total=.6)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


@async_timed()
async def main():
    """Задание таймаута в aiohttp."""
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.5)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://ya.ru')


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
