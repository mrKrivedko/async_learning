import time
from typing import Callable


def sync_timed(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f'функция {func.__name__} завершилась за {(end - start):.4f} сек.'
        )
        return result
    return wrapper
