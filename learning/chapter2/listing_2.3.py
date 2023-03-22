import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1

# asyncio.run - задумана как главная точка входа
#  в созданное приложение asyncio. Она выполняет только одну сопрограмму,
# и эта сопрограмма должна позаботиться обо всех остальных аспектах приложения.
result = asyncio.run(coroutine_add_one(1))

print(result)
