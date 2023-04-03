import asyncio
import asyncpg
from asyncpg.connection import Connection
from asyncpg.cursor import Cursor


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count = item_count + 1
        yield item


async def main():
    """
    Получение заданного числа элементовв с помощью асинхронного генератора.
    """
    connection: Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products'
    )
    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        product_generator: Cursor = connection.cursor(query)
        async for product in take(product_generator, 5):
            print(product)
        print('Получены все пять товаров!')
    await connection.close()


asyncio.run(main())
