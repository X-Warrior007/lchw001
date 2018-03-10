import threading
import time


class myThread(threading.Thread):
    """1 集成Thread 2 实现其中run方法 3 创建该类的实例对象 4对象.start()启动创建和执行"""
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)  # name属性中保存的是当前线程的名字
            print(msg)

if __name__ == '__main__':
    for i in range(5):
        mt = myThread()
        mt.start()  #　创建子线程　在子线程中调用ｒｕｎ方法

    # 多个线程执行的时候　　顺序是随机　无序的
    # while True:
    #     time.sleep(1)
    #     print("主线程正在执行")