import asyncio
import concurrent.futures
import functools
import time

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
        second: dict[str, int],
) -> dict[int, str]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


@async_timed()
async def main(partition_size: int):
    """Распараллеливание с помощью MapReduce и пула процессов."""
    print('Экзекуция началась!')
    start_open = time.time()
    with open(
        'googlebooks-eng-all-1gram-20120701-a', encoding='utf-8'
    ) as file:
        end_open = time.time()
        print(f'йа аткрылься за {(end_open - start_open):.4f} сек.')

        start_read = time.time()
        contents = file.readlines()
        # print(contents[0])  # A'Aang_NOUN     1879    45      5
        # print(len(contents))  # 86_618_505
        end_read = time.time()
        print(f'йа прачеталься за {(end_read - start_read):.4f} сек.')

        loop = asyncio.get_running_loop()
        tasks = []
        start_futures = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(
                    pool, functools.partial(map_frequencies, chunk)
                ))

            intermediate_results = await asyncio.gather(*tasks)
            print('асинхронно отмапались, редуцируем..')
            start_reduce = time.time()
            final_result = functools.reduce(
                merge_dictionaries,
                intermediate_results
            )
            end_reduce = time.time()

            print(
                f'задачи завершились за {(end_reduce - start_reduce):.4f} сек.'
            )
            print(f'atom1c встречается {final_result.get("atom1c")} раз.')
            print(len(final_result))
            # atom1c встречается 243 раз.

            end_futures = time.time()
            print(
                f'время выполнения: {(end_futures - start_futures):.4f} секунд'
            )


if __name__ == '__main__':
    asyncio.run(main(partition_size=870000))
    print('канец!')
