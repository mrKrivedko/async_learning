import asyncio

from util import delay


async def main():
    """Задание тайм-аута для задачи с помощью wait_for"""
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('timeout!!')
        print(f'Задача была снята? {delay_task.cancelled()}')


asyncio.run(main())
