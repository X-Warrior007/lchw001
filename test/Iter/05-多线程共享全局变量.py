import threading
import time

g_number = 0

# 创建一把全局互斥锁
g_lock = threading.Lock()

def worker1():
    global g_number
    for i in range(1000000):

        # 尝试获取并且加锁　如果没有被锁定　就可以被我锁定；　
        # 如果已经被锁定　阻塞等待　直到成功获取并且锁定　
        g_lock.acquire()
        g_number += 1

        # 释放锁资源　解锁　　未锁定　－－－－> 未锁定状态
        g_lock.release()
        # print(g_number)

def worker2():
    global g_number
    for i in range(1000000):
        g_lock.acquire()
        g_number += 1
        g_lock.release()
        # time.sleep(1)


if __name__ == '__main__':
    thd1 = threading.Thread(target=worker1)
    thd1.start()

    thd2 = threading.Thread(target=worker2)
    thd2.start()

    thd1.join()
    thd2.join()
    print("比赛的结果是%d" % g_number)
    # 多个线程同时修改同一个数据　会引起异常
