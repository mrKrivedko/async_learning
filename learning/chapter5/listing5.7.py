import asyncio
import asyncpg

from commands_sql import PRODUCT_QUERY


async def query_product(pool: asyncpg.Pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(PRODUCT_QUERY)


async def main():
    """Создание пула подключений и конкурентноре выполнение запросов."""
    # создать пул с шестью подключениями
    async with asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products',
        min_size=6,
        max_size=6
    ) as pool:
        # конкурентно выполнить два запроса
        await asyncio.gather(
            query_product(pool),
            query_product(pool)
        )


asyncio.run(main())
