import asyncio
from util import async_timed, delay


@async_timed()
async def main():
    """
    Неправильное использование спискового включения
    для создания и ожидания задач.
    """
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

# asyncio.run(main())

# в windows нужно управлять циклом событий вручную
# asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
