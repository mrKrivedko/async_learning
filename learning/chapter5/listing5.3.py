import asyncio
import asyncpg

import commands_sql


async def main():
    """Использование сопрограммы execute для выполнения комманд create."""
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password=''
    )
    statements = [
        commands_sql.CREATE_BRAND_TABLE,
        commands_sql.CREATE_PRODUCT_TABLE,
        commands_sql.CREATE_PRODUCT_COLOR_TABLE,
        commands_sql.CREATE_PRODUCT_SIZE_TABLE,
        commands_sql.CREATE_SKU_TABLE,
        commands_sql.SIZE_INSERT,
        commands_sql.COLOR_INSERT
    ]

    print('Создается база данных product..')
    for statement in statements:
        print(statement)
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана!')
    await connection.close()


asyncio.run(main())
