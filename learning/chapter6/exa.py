import asyncio
from asyncio import Future
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


async def reading(data: TextIO, chunk_size):
    """Считываем по частям."""
    contents = []
    count = 0
    finish = False
    while not finish:
        line = data.readline()
        if line:
            contents.append(line)
            count += 1
        if count == chunk_size:
            count = 0
            yield contents
        elif not line:
            finish = True
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
        async for contents in reading(file, chunk_size):
            loop = asyncio.get_running_loop()
            tasks = []
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
        fin = functools.reduce(merge_dictionaries, final_result)
        print(f'atom1c встречается {fin.get("atom1c")} раз.')

        end = time.time()
        print(f'время выполнения tasks of pool: {(end - start):.4f} секунд')


if __name__ == '__main__':
    asyncio.run(main(partition_size=250_000, chunk_size=10_000_000)) # 90 sec.
    # (partition_size=40_000, chunk_size=43_309_252))
