import asyncio
import asyncpg

from util import async_timed
from commands_sql import PRODUCT_QUERY


async def query_product(pool: asyncpg.Pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(PRODUCT_QUERY)


@async_timed()
async def query_products_sync(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_products_concurent(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


@async_timed()
async def main():
    """Синхронное и конкурентное выполнение запросов."""
    async with asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products',
        min_size=6,
        max_size=6
    ) as pool:
        await query_products_sync(pool, 10000)
        await query_products_concurent(pool, 10000)


asyncio.run(main())
