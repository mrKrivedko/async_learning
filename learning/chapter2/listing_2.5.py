import asyncio


async def hello_world_message() -> str:
    # Приостановить hello_world_message на 1 с.
    await asyncio.sleep(1)
    return 'Hello world!'


async def main() -> None:
    # Приостановить main до завершения hello_world_message
    message = await hello_world_message()
    print(message)


asyncio.run(main())
