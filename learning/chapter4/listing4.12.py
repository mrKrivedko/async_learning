import aiohttp
import asyncio
import logging

from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    """Отмена работающих запросов при возникновении исключения."""
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'python://bad.com')),
            asyncio.create_task(fetch_status(session, 'https://ya.ru', 3)),
            asyncio.create_task(fetch_status(session, 'https://ya.ru', 3))
        ]
        done, pending = await asyncio.wait(
            fetchers,
            return_when=asyncio.FIRST_EXCEPTION
        )

        print(f'Количество завершившихся задач: {len(done)}')
        print(f'Количество ожидающих задач: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    'При выполнении запроса возникло исключение',
                    exc_info=done_task.exception()
                )

        for pending_task in pending:
            pending_task.cancel()


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())

# Приложение не заняло почти никакого времени,
# потому что мы быстро отреагировать на то,
# что один из запросов возбудил исключение;
# прелесть этого режима в том, что реализуется тактика быстрого отказа,
# те быстрой реакции на возникающие проблемы.
