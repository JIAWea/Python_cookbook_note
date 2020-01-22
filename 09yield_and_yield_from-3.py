# 协程的工作模式

# 特点：
# 同一线程内，实际上是子程序的切换而不是线程的切换，没有线程切换的开销
# 共享资源不必加锁，只需要判断状态，不存在同时写变量的冲突，效率高


def consumer():
    r = ''
    while True:
        n = yield r
        # print('[Consumer]: r:{}, n:{}'.format(r, n))
        if not n:
            return
        print('[Consumer]: consuming {}...'.format(n))
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 3:
        n = n + 1
        print('[Produce]: producing {}...'.format(n))
        r = c.send(n)
        print('[Produce]: consumer return {}'.format(r))
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
