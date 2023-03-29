import asyncio
import aiohttp
import logging

from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    """Обработка исключений при использовании wait."""
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://ya.ru')
        bad_request = fetch_status(session, 'python://bad.ru')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f'Количество завершившихся задач: {len(done)}')
        print(f'Количество ожидающих задач: {len(pending)}')

        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    'При выполнении запроса возникло исключение.',
                    exc_info=done_task.exception()
                )


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
