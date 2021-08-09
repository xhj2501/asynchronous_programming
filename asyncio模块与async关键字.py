import asyncio

"""遇到IO自动切换"""


# @asyncio.coroutine  # 装饰器(py3.5以后不用)
async def func1():
    print(1)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务
    print(2)


# @asyncio.coroutine  # 装饰器(py3.5以后不用)
async def func2():
    print(3)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动切换到tasks中的其他任务
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
