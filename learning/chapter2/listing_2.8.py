import asyncio

from util import delay


async def main():
    # создали таску (запланировали задачу, но не выполняем)
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    # блокируем main до выполнения таски
    result = await sleep_for_three
    # обязательно нужно использовать await для задачи
    print(result)


asyncio.run(main())
