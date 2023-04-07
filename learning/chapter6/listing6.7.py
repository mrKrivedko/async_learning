import time

from util import timed


@timed
def frequency(lines: list, frequencies: dict):
    print('йа думою!')

    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = count
    print(len(frequencies))


@timed
def main():
    """Подсчет частот слов, начинающихся буквой a."""
    print('Экзекуция началась!')
    start = time.time()
    frequencies = {}

    with open(
        'googlebooks-eng-all-1gram-20120701-a', encoding='utf-8'
    ) as file:
        lines = file.readlines()
        end = time.time()
        total = end - start
        print(f'file opened to {total:.4f} seconds!')
        frequency(lines, frequencies)


if __name__ == '__main__':
    main()
    print('канец!')
