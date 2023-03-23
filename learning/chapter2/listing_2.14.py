from asyncio import Future


"""Основы будущих объектов Future"""


my_future = Future()

print(f'my_future готов? {my_future.done()}')

my_future.set_result(42)

print(f'my_future готов? {my_future.done()}')

#  мы не вызываем метод result, прежде чем результат установлен.
print(f'Каков результат хранится в my_future? {my_future.result()}')
