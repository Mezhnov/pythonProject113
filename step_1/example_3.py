from asyncio import run, sleep, create_task


async def my_async_func():
    print('Запуск ...')
    await sleep(1)
    print('... Готово!')


async def my_main_func():
    task = create_task(my_async_func())
    await task


run(my_main_func())
