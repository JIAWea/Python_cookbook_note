# 阅读了Python cookbook中的4.13，其中使用到了yield 和 yield from，一直对这两者之间的用法不是很清楚
# 这里顺便了解一下。

# 函数可以看成是一堆指令的集合。在函数中加入 yield 可以把一个函数变成一个 generator，虽然调用的方式不一样了，
# 但是其实现的功能和原来的函数基本是一样的。generator 看起来像函数调用，但不会执行任何函数代码，知道对其调用
# next() （在for循环中会自动调用）才开始执行。执行流程虽然跟函数一样，但每执行到一个 yield 语句就会中断，并返
# 回一个迭代值，下次执行时从 yield 的下一个语句继续执行，看起来就像一个函数在正常执行中被 yield 中断了数次。

# 练习：
# 1 打印出斐波那契数列
from inspect import isgeneratorfunction


def fab(num):
    n, a, b = 0, 0, 1
    while n < num:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1


# 2 用 yield 读取大文件
def read_file(path, block_size=100):
    with open(path, 'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                return


# ############################################
# yield 和 yield from 用法对比
# 3 使用 yield 拼接可迭代对象
def gen_yield(*args):
    for item in args:
        for i in item:
            yield i


def gen_yield_from(*args):
    for item in args:
        yield from item


# 由上面两种方式对比，可以看出，yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，
# 对比yield来说代码更加简洁，结构更加清晰。

if __name__ == '__main__':
    # gen = fab(6)                # <generator object fab at 0x00000000021047C8>
    # for i in gen:
    #     print(i, end=" ")

    # 判断是否为 generator 函数
    # print(isgeneratorfunction(fab))         # True

    a_str = 'ABC'
    a_list = [1, 2, 3]
    a_dict = {'name': 'ray', 'age': 18}

    new_yield_list = gen_yield(a_str, a_list, a_dict, (4, 5, 6, 7))
    print("new_yield_list:", list(new_yield_list))

    new_yield_from_list = gen_yield_from(a_str, a_list, a_dict, (4, 5, 6, 7))
    print("new_yield_from_list:", list(new_yield_from_list))
