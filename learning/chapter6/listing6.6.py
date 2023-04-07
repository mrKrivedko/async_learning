import functools

from util import timed


@timed
def map_frequency(text: str) -> dict:
    words = text.split(' ')
    words = [word.lower() for word in words]
    print(words)
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies


@timed
def merge_dictionares(
        first: dict[str, int],
        second: dict[str, int]
) -> dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


lines = [
    'I know what I know',
    'I know that I know',
    'I dont know much',
    'They dont know much'
]


@timed
def main():
    """Однопоточная модель MapReduce."""
    mapped_results = [map_frequency(line) for line in lines]

    for result in mapped_results:
        print(result)

    print(functools.reduce(merge_dictionares, mapped_results))


if __name__ == '__main__':
    main()
