import multiprocessing
from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f'Привет, {name}!'


if __name__ == '__main__':
    # вывести количество процессорных ядер
    print(multiprocessing.cpu_count())
    # создать пулл процессов
    with Pool() as process_pool:
        # метод apply() блокирует выполнение, пока функция не завершится.
        hi_jeff = process_pool.apply(say_hello, args=('Jeff', ))
        hi_john = process_pool.apply(say_hello, args=('John', ))
        print(hi_jeff)
        print(hi_john)
