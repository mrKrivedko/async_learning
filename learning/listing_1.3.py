import threading


def hello_from_thread() -> None:
    print(f'Привет от потока {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)

# Запускаем поток
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'В данный момент python выполняет {total_threads} поток(ов).')
print(f'Имя текущего потока {thread_name}')

# join приостанавливает программу,
# до тех пор пока указанный поток не завершится.
hello_thread.join()
