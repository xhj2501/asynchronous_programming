import asyncio


async def f():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "请回复"


async def main():
    print("main开始")

    task_list = [
        asyncio.create_task(f(), name='n1'),
        asyncio.create_task(f(), name='n2')
    ]

    print("main结束")

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done)


asyncio.run(main())

# task_list=[f(),f()]
#
# done,pending=asyncio.run(asyncio.wait(task_list))
# print(done)
