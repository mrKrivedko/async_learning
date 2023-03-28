import asyncio
import aiohttp

from util import async_timed, delay
from chapter_4 import fetch_status


@async_timed()
async def main():
    """Завершение допускающих ожидание объектов не по порядку."""
    # недетерминированный порядок выполнения
    results = await asyncio.gather(delay(3), delay(1))
    # вернет детерменированный порядок результатов
    print(results)


@async_timed()
async def exception_example_one():
    """
    Пример обработки исключений в asyncio.gather с return_exceptions=False.
    """
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        # Исключение возникает в точке, где мы ждем gather с помощью await
        status_codes = await asyncio.gather(*tasks)
        print(status_codes)


@async_timed()
async def exception_example_two():
    """
    Пример обработки исключений в asyncio.gather с return_exceptions=True.
    """
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        # Исключения не возбуждаются,
        # а возвращаются в одном списке с результатами.
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [
            result for result in results if isinstance(result, Exception)
        ]
        succesful_results = [
            result for result in results if not isinstance(result, Exception)
        ]
        print(f'Все результаты: {results}')
        print(f'Завершились успешно: {succesful_results}')
        print(f'Завершилось с исключением: {exceptions}')


# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())

asyncio.get_event_loop().run_until_complete(exception_example_two())

asyncio.get_event_loop().run_until_complete(exception_example_one())
