import asyncio
import time
import functools
from typing import TextIO, Generator


def reading(file: TextIO, chunk_size):
    """Читаем файл и делим на чанки."""
    with open(file, encoding='utf-8') as opened_file:
        partial_files = []
        bank = []
        for line in opened_file:
            if len(bank) == chunk_size:
                bank = tuple(bank)
                partial_files.append(bank)
                bank = []
            bank.append(line)
        bank = tuple(bank)
        partial_files.append(bank)
        opened_file.close()
        return partial_files


def reading_file(file: str):
    with open(file, encoding='utf-8') as file:
        return file.readlines()


google = 'googlebooks-eng-all-1gram-20120701-a'
words = 'common_words.txt'


def main(chunk_size: int):
    start = time.time()
    data = tuple(reading(google, 10000000))
    # data = reading_file(google)
    print(len(data))
    end = time.time()
    print(f'прочитали и разбили на части за {(end - start):.4f} секунд.')
    # print(part_data)
    print('reduce run')
    start = time.time()
    # print(functools.reduce((lambda x, y: x + y), data))
    end = time.time()
    print((f'reduce to: {(end - start):.4f} секунд.'))


if (name := __name__) == '__main__':
    start = time.time()
    main(0)
    end = time.time()
    print(f'{name} завершилась за {(end - start):.4f} секунд.')
