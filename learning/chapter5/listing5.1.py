import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='postgres',
        password='password'
    )
    version = connection.get_server_version()
    print(f'postgres version: {version}')
    await connection.close()


asyncio.run(main())
