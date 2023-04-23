from asyncio import run, sleep


async def myAsyncFunc():
    print('Запуск ...')
    await sleep(1)
    print('... Готово!')


async def my_main_func():
    await myAsyncFunc()


run(my_main_func())
