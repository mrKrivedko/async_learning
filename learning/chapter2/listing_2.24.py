import asyncio


async def main():
    """Изменение продолжительности медленного обратного вызова."""
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250


asyncio.run(main())
