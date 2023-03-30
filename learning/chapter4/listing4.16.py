import asyncio
import aiohttp

from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    """Отмена медленного запроса."""
    async with aiohttp.ClientSession() as session:
        URL = 'http://ya.ru'

        request_one = fetch_status(session, URL)
        request_two = fetch_status(session, URL, delay=3)

    # request_one = asyncio.create_task(fetch_status(session, URL))
    # request_two = asyncio.create_task(fetch_status(session, URL, delay=3))

        done, pending = await asyncio.wait(
            [request_one, request_two],
            timeout=1
        )

        for task in pending:
            # если request_one и request_two не обернуть задачей, то сравнение
            # будет некорректным. Когда wait передаются сопрограммы,
            # они автоматически оборачиваются задачами и возращенные
            # done и pending будут содержать задачи.
            # Получается что мы сравниваем задачу (task) с сопрограммой
            if task is request_two:
                print('request_two so slow..')
                task.cancel()


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
