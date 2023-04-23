from asyncio import run, sleep, create_task


async def callee():
    await sleep(3)
    print('Привет, ')


async def caller():
    print('Запускаем первую сопрограмму и НЕ ждем ее завершения')
    create_task(callee())
    print('Запускаем вторую сопрограмму и НЕ ждем ее завершения')
    create_task(sleep(3))
    print('друг')


run(caller())
