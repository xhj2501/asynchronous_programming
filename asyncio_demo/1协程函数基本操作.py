import asyncio


async def f():
    # 定义协程函数
    print("hello world!")


result = f()  # 获得协程对象

asyncio.run(result)  # 通过事件循环处理协程对象，执行协程函数代码(py3.7)
