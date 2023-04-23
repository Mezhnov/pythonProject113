from asyncio import run, sleep


async def callee():
    await sleep(3)
    print('Привет, ')


async def caller():
    print('Запускаем первую сопрограмму и ждем ее завершения')
    await callee()
    print('Запускаем вторую сопрограмму и ждем ее завершения')
    await sleep(3)
    print('друг')


run(caller())
