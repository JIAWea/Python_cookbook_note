# yield 除了能生成一个生成器的作用，还能用在协程当中，当我们遇到了阻塞，如 IO 阻塞时，可以调配线程去做别的事情

# 下面有一段伪代码，如：
"""
def test():
    request_google_server(data)
    yield
    print(data)
"""
# 去请求百度需要走很长的网络线路，三路握手，数据传递。这在 cpu 的感官里这就是等待数年的操作。我们的程序无法继续运行，
# 难道我们就这样让 cpu 等待？当然不所以调用 yield 把线程的控制权交出来，然后我们让线程去做一些其他的事情，比如再入
# 请求新浪服务器等等，一瞬间我们同时请求了 N 台服务器了。

# 稍微总结一下 yield，通过其可以让我们程序员实现对线程的调配，从而更加充分的利用 cpu。


# 通常一个函数都是 a 调用 b， b 调用 c， c 调用 a。这样才会增加代码的可读性，复用性。
# 假如 b() 调用 c()， c()中存在 yield 时我们应该如何处理呢？

def b():
    gen = c()
    r = gen.send(None)          # send(None) 相当于 next()
    print(r)                    # 1
    r = gen.send(None)
    print(r)                    # 2


def c():
    yield 1
    yield 2
    yield 3


# 鉴于生成器中调用生成器比较麻烦，所有有了 yield from 语法。用于简化嵌套调用生成器的语法复杂度，如：

def b2():
    r = yield from c2()
    print("r of b2:", r)            # 4 （c2的return值）


def c2():
    r = yield 1
    print("r of c2:", r)            # r of b2: 哈哈
    return 4


if __name__ == '__main__':
    # b()
    try:
        gen = b2()
        # 第一次 send 返回的是 1，b2()到了 yield from 后，控制权就到了我们这里，所以返回了c2()中的 yield 1
        gen.send(None)
        # 第二次 send 值在上次 停留在 c2() 停留的 yield 开始往下执行，把 “哈哈” 作为 yield 的返回值
        gen.send("哈哈")
    except StopIteration:
        print("Stop")

