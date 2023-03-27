import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

SERVER_ADDRESS = ('127.0.0.1', 8000)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen()

connections = []

try:
    while True:
        # accept блокирующий вызов (ожидает подключения)
        connection, client_address = server_socket.accept()
        print(f'Получен запросна подключение от {client_address}!')
        connections.append(connection)

        for connection in connections:
            buffer = b''

            while buffer[-2:] != b'\r\n':
                # recv, тоже блокирующий вызов (ожидает приема сообщения)
                data = connection.recv(2)
                if not data:
                    break
                else:
                    print(f'Получены данные: {data}!')
                    buffer += data

            print(f'Все данные: {buffer}')
            connection.sendall(buffer)
finally:
    server_socket.close()
