import asyncio
import concurrent.futures
import functools
import time
from typing import TextIO, List, Dict

from util import async_timed


def partition(
        data: list,
        chunk_size: int,
) -> list:
    for i in range(0, len(data), chunk_size):
        yield data[i: i + chunk_size]


def map_frequencies(chunk: list[str]) -> dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(
        first: dict[str, int],
        second: dict[str, int]
) -> dict[int, str]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


def reading(data: TextIO, chunk_size):
    """Считываем по частям."""
    contents = []
    count = 0
    full = 0
    for line in data:
        count += 1
        full += 1
        # print(f'{count}: {line}')
        contents.append(line)
        if line == '':
            print('pusto')
            print(full)
            return contents
        elif count == chunk_size:
            count = 0
            print(full)
            yield contents


@async_timed()
async def main(
        partition_size: int,
        chunk_size: int
):
    """Распараллеливание с помощью MapReduce и пула процессов."""
    with open(
        'googlebooks-eng-all-1gram-20120701-a', encoding='utf-8'
    ) as file:
        final_result = []
        start = time.time()
        # contents = file.readlines()
        for contents in reading(file, chunk_size):
            print(f'длина: {len(contents)}')
            # print(contents)
            loop = asyncio.get_running_loop()
            tasks = []
            start = time.time()
            with concurrent.futures.ProcessPoolExecutor() as pool:
                for chunk in partition(contents, partition_size):
                    tasks.append(loop.run_in_executor(
                        pool, functools.partial(map_frequencies, chunk)
                    ))

                intermediate_results = await asyncio.gather(*tasks)

                reduce_result = functools.reduce(
                    merge_dictionaries, intermediate_results)
                final_result.append(reduce_result)
                contents.clear()
        print(len(final_result))
        for r in final_result:
            print(len(r))
        fin = functools.reduce(merge_dictionaries, final_result)
        print(len(fin))
        print(f'atom1c встречается {fin.get("atom1c")} раз.')

        end = time.time()
        print(f'время выполнения: {(end - start):.4f} секунд')


if __name__ == '__main__':
    asyncio.run(main(partition_size=800_000, chunk_size=10000_000))
