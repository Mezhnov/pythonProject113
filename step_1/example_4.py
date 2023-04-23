from asyncio import get_event_loop, wait, sleep


async def async_func(task_no):
    print(f'{task_no}: Запуск ...')
    await sleep(3)
    print(f'{task_no}: ... Готово!')


async def main():
    task_a = loop.create_task(async_func('task_a'))
    task_b = loop.create_task(async_func('task_b'))
    task_c = loop.create_task(async_func('task_c'))
    await wait([task_a, task_b, task_c])


if __name__ == "__main__":
    try:
        loop = get_event_loop()
        loop.run_until_complete(main())
    except Exception:
        pass

