async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f'Результат функции: {function_result}, а тип: {type(function_result)}')
print(
    f'Результат сопрограммы: {coroutine_result},'
    f' а тип: {type(coroutine_result)}'
)

# Сопрограммы не выполняются, если их вызвать на прямую.
# Вместо этого возвращаается обьект сопрограммы, который будет выполнен позже.
