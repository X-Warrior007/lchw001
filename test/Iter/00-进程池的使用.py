import multiprocessing
import time
import os
import random

# 1 理解进程池的工作模式<好处 节约进程的创建和销毁的系统开销 可以更快的响应用户需求>
# 2 添加任务的两种的区别

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg,os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

if __name__ == '__main__':
    # 1 创建进程池 参数表示最多可以创建多少个进程<工作进程>
    pool = multiprocessing.Pool()

    # 2 添加任务
    # apply添加方式 阻塞等待刚刚添加的任务 执行完成 才会继续往下执行-阻塞添加方式
    pool.apply(func=worker,args=('111',))
    print("任务执行完")
    pool.apply(func=worker, args=('222',))

    # 非阻塞的任务添加方式 只管添加任务 不会阻塞等待任务执行完成
    pool.apply_async(func=worker, args=('333',))
    pool.apply_async(func=worker, args=('444',))
    # 3 关闭进程池 ----  不再允许添加新的任务
    pool.close()

    # 直接全部终止 工作进程
    # pool.terminate()

    # 4 阻塞等待所有任务执行完成
    # 只要主进程一退出 所有正在执行的任务全部终止
    pool.join()
    print("所有任务都执行完成了")


