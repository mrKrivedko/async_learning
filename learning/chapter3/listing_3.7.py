import selectors
import socket

from selectors import SelectorKey


selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)
with server_socket as server:
    while True:
        # создаем селектор с таймаутом 1с
        events: list[tuple[SelectorKey, int]] = selector.select(timeout=1)

        if len(events) == 0:
            print('Событий нет, ждем-с')

        for event, _ in events:
            # получить сокет для которого произошло событие
            event_socket = event.fileobj

            # если событие произошло с серверным сокетом,
            # значит, была попытка подключения
            if event_socket == server:
                connection, client_address = server.accept()
                connection.setblocking(False)
                print(f'Получени запрос на подключение от {client_address}')
                # регистрируем клиент, подключившийся к сокету
                selector.register(connection, selectors.EVENT_READ)
            else:
                data = event_socket.recv(1024)
                print(f'Получены данные: {data}')
                event_socket.send(data)
