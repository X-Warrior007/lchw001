import time
import threading


def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    print(threading.enumerate())
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        # saySorry()
        # 创建一个线程

        # 创建一个线程执行的计划 target指定线程在执行时 执行的函数
        thd = threading.Thread(target=saySorry)

        # 启动计划 -- 创建并且执行子线程
        thd.start()

    # 查看当前进程内部存活的所有的线程列表 《主线程 子线程》 ----> len(列表) 线程数量
    # [<_MainThread(MainThread, started 139901408708352)>,
    # <Thread(Thread-1, started 139901382989568)>,
    #  <Thread(Thread-2, started 139901374596864)>,
    # <Thread(Thread-4, started 139901357811456)>,
    # <Thread(Thread-5, started 139901349418752)>,
    # <Thread(Thread-3, started 139901366204160)>]

    # print(threading.enumerate())
    # while True:
    #     if len(threading.enumerate()) == 1:
    #         print("所有的子线程都退出了")
    #         break
    #     else:
    #         time.sleep(1)

    # 默认情况下 主线程会等待所有的子线程退出之后再退出
