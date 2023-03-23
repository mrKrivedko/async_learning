from asyncio import Future
import asyncio


def make_request() -> Future:
    future = Future()
    # Создать задачу, которая асинхронно установит значение future.
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future) -> None:
    print(0)
    # Ждать 1с, прежде чем установить значение.
    await asyncio.sleep(1)
    print(1)
    future.set_result(42)


async def main():
    """Ожидание будущего объекта."""
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    # Приостановить main, пока значение future не установлено
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())
