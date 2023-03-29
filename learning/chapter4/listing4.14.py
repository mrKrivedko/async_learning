import aiohttp
import asyncio

from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    """Обработка всез результатов по мере поступления."""
    async with aiohttp.ClientSession() as session:
        URL = 'https://ya.ru'
        pending = [
            asyncio.create_task(fetch_status(session, URL)),
            asyncio.create_task(fetch_status(session, URL)),
            asyncio.create_task(fetch_status(session, URL))
        ]
        while pending:
            done, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED
            )

            print(f'Количество завершившихся задач: {len(done)}')
            print(f'Количество ожидающих задач: {len(pending)}')

            for done_task in done:
                print(await done_task)


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
