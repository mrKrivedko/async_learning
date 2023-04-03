import asyncio
import asyncpg


async def main():
    """Потоковая обработка результатов."""
    connection: asyncpg.connection.Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products'
    )
    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())
