"""实际编译不通过"""
from greenlet import greenlet


def func1():
    print(1)  # S2：输出1
    gr2.switch()  # S3：切换到func2函数
    print(2)  # S6：输出2
    gr2.switch()  # S7：输出1


def func2():
    print(3)  # S4：输出3
    gr1.switch()  # S5：切换到func1函数，从上一次执行的位置继续向后执行
    print(4)  # S8：输出4


gr1 = greenlet(func1())
gr2 = greenlet(func2())

gr1.switch()  # S1：去执行func1函数
