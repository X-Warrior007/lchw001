from time import sleep
import threading

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    sing_thd = threading.Thread(target=sing)
    sing_thd.start()

    dance_thd = threading.Thread(target=dance)
    dance_thd.start()

    # while True:
    #     if len(threading.enumerate()) == 1:
    #         print("所有的子线程都退出了")
    #         break
    #     else:
    #         sleep(1)

    # 在主线程阻塞等待 Thread对象标识的子线程退出之后 才会继续往下执行代码
    sing_thd.join()
    dance_thd.join()

    print("太棒了")