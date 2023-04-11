import asyncio
from asyncio import Future
from typing import TextIO, Generator

import aiofiles


async def reading(file: str, chunk_size: int):
    """корутина на чтение"""
    async with aiofiles.open(file, mode='r', encoding='utf-8') as file:
        content = []
        count = 0
        async for line in file:
            if count == chunk_size:
                count = 0
                content.append(line)
                yield content
            count += 1
            content.append(line)
            yield line


def reading_file(file: str):
    with open(file, encoding='utf-8') as file:
        return file.readlines()


google = 'googlebooks-eng-all-1gram-20120701-a'
words = 'common_words.txt'


async def main():
    result = []
    lines = reading_file(words)
    # async for line in lines:
    #     # print(len(line))
    #     result.append(line)
    print(len(lines))


if __name__ == '__main__':
    asyncio.run(main())
