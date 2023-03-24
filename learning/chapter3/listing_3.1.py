import socket


SERVER_ADRESS = ('127.0.0.1', 8000)

# создать TCP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# через setsockport установим флаг SO_REUSADDR в 1,
# это позволит повторно использовать номер порта,
# после того как мы остановим и заново запустим приложение.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# заздать адресс сокета 127.0.0.1:8000
server_socket.bind(SERVER_ADRESS)
# прослушивать запросы на подключение
server_socket.listen()

# дождаться подключения и выделить клиентский сокет
connection, client_address = server_socket.accept()
print(f'Получен запрос на подключение от {client_address}!')
