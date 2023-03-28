import asyncio
import socket
import logging
from asyncio import AbstractEventLoop


async def echo(
        connection: socket.socket,
        loop:  AbstractEventLoop
) -> None:
    """Сопрограмма для обработки данных от сокета."""
    try:
        # в бесконечном цикле ожидаем данных от клиента.
        while data := await loop.sock_recv(connection, 1024):
            if data == b'boom\r\n':
                raise Exception('Ошибка сети')
            # получив данные, отправляем их обратно клиенту
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def listen_for_connection(
        server_socket: socket.socket,
        loop: AbstractEventLoop
) -> None:
    """Сопрограмма для прослушивания подключения к серверу."""
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        # после получения запроса на подключение, создаем задачу echo,
        # ожидающую данные от клиента
        asyncio.create_task(echo(connection=connection, loop=loop))


async def main():
    """Построение асинхронного эхо-сервера."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('192.168.0.154', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
