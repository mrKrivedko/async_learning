import asyncio
import asyncpg
from asyncpg.transaction import Transaction


async def main():
    """Ручное управление транзакцией."""
    connection: asyncpg.connection.Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='',
        database='products'
    )
    # Создать экземпляр транзакции
    transaction: Transaction = connection.transaction()
    # Начать транзакцию
    await transaction.start()
    try:
        await connection.execute(
            "INSERT INTO brand"
            "VALUES(DEFAULT, 'brand_1')"
        )
        await connection.execute(
            "INSERT INTO brand"
            "VALUES(DEFAULT, 'brand_2')"
        )
    except asyncpg.PostgresError:
        print('Ошибка транзакция откатывается!')
        # Если было исключение, откатить
        await transaction.rollback()
    else:
        print('Ошибки нет, транзакция фиксируется.')
        # Если небыло исключения, зафиксировать
        await transaction.commit()
    query = """
        SELECT brand_name FROM brand
        WHERE brand_name LIKE 'brand%'
    """
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())
