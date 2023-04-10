import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


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


async def reduce(loop, pool, counters, chunk_size) -> dict[str, int]:
    chunks: [List[List[Dict]]] = list(partition(counters, chunk_size))
    reducers = []
    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = functools.partial(
                functools.reduce,
                merge_dictionaries,
                chunk
            )
            reducers.append(loop.run_in_executor(pool, reducer))
        reducer_chunks = await asyncio.gather(*reducers)
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()
    return chunks[0][0]


async def main(partition_size: int):
    """Распараллеливание операции reduce."""
    with open(
        'googlebooks-eng-all-1gram-20120701-a', encoding='utf-8'
    ) as file:
        contents = file.readlines()
        print(len(contents))
        loop = asyncio.get_running_loop()
        tasks = []
        with concurrent.futures.ProcessPoolExecutor() as pool:
            start = time.time()

            for chunk in partition(contents, partition_size):
                tasks.append(
                    loop.run_in_executor(
                        pool,
                        functools.partial(map_frequencies,
                                          chunk)
                    )
                )
            intermediate_results = await asyncio.gather(*tasks)
            final_result = await reduce(loop, pool, intermediate_results, 500)

            print(f'atom1c встречается {final_result.get("atom1c")} раз')

            end = time.time()
            print(
                f'map reduce завевшилось за {(end - start):.4f} сек.'
            )


if __name__ == '__main__':
    asyncio.run(main(partition_size=850_000))
