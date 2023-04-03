import asyncio
import asyncpg


async def main():
    """Создание транзакции."""
    connection: asyncpg.connection.Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products'
    )
    # Начать транзакцию базы данных
    async with connection.transaction():
        await connection.execute(
            """
                INSERT INTO brand
                VALUES(DEFAULT, 'brand_1')
            """
        )
        await connection.execute(
            """
                INSERT INTO brand
                VALUES(DEFAULT, 'brand_2')
            """
        )
    query = """
        SELECT brand_name
        FROM brand
        WHERE brand_name LIKE 'brand%'
    """
    # Выбрать марки и убедиться, что транзакция была зафиксирована
    brands = await connection.fetch(query)
    print(brands)
    await connection.close()


asyncio.run(main())
