import asyncio
import asyncpg
from asyncpg.connection import Connection
from asyncpg.cursor import Cursor


async def main():
    """Перемещение по курсору и выборка записей."""
    connnection: Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products'
    )
    async with connnection.transaction():
        query = 'SELECT product_id, product_name from product'
        # Создаем курсор для запроса
        cursor: Cursor = await connnection.cursor(query)
        # Сдвинем курсор на 500 записей вперед
        await cursor.forward(500)
        # получаем следующие 100 записей
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connnection.close()


asyncio.run(main())
