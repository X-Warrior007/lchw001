import time

# 切换着执行  yield

def worker1():
    # for i in range(n):
    while True:
        print("in worker1")
        yield
        time.


def worker2():
    # for i in range(n):
    while True:
        print("in worker2")
        yield
        time.sleep(1)

if __name__ == '__main__':
    # 调用生成器函数 产生生成器对象
    w1 = worker1()
    w2 = worker2()

    while True:
        next(w1)
        next(w2)