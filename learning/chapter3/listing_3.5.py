import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
# пометить серверный сокет как неблокирующий
server_socket.setblocking(False)

connections: list[socket.socket] = []

try:
    while True:
        connection, client_address = server_socket.accept()
        # пометить клиентский сокет как неблокирующий
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {client_address}')
        connections.append(connection)

        for connection in connections:
            buffer = b''

            while buffer[-2:] != b'\r\n':
                data = connection.sendall(buffer)
finally:
    server_socket.close()
