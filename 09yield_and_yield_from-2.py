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
