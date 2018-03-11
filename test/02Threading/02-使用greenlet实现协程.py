import time
from greenlet import greenlet

def worker1():
    # for i in range(n):
    while True:
        print("in worker1")
        # 切换到第二个协程执行
        g2.switch()
        time.sleep(1)


def worker2():
    # for i in range(n):
    while True:
        print("in worker2")
        # 切换到第一个协程执行
        g1.switch()
        time.sleep(1)

# 创建协程对象
g1 = greenlet(worker1)
g2 = greenlet(worker2)
# 切换到协程执行
g1.switch()