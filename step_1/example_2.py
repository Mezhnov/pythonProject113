from asyncio import run, sleep


async def my_async_func():
    print('Запуск ...')
    await sleep(1)
    print('... Готово!')


async def my_main_func():
    await my_async_func()


run(my_main_func())
