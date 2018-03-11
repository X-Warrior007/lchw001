from gevent import monkey
monkey.patch_all()  # patch就是破解 gevent建议破解在第二行
import gevent
import time

# 在默认情况 gevent不会自动切换协程
# 可以使用gevent提供的工具 将recv recvfrom time.sleep acccept等函数(默认会阻塞) -----input不能破解
# 变成不再阻塞程序
def worker1(n):
    for i in range(n):
        print("in worker %s" % gevent.getcurrent())
        time.sleep(0.3)


# 创建一个协程对象 并且开始运行
g1 = gevent.spawn(worker1,10)
g2 = gevent.spawn(worker1,10)
g3 = gevent.spawn(worker1,10)

# 阻塞等待协程执行完成
# g1.join()
# g2.join()
# g3.join()
# 等待所有的协程执行完成的目的  -----> 保持主进程的存活
gevent.joinall([g1,g2,g3])
# time.sleep(100)
