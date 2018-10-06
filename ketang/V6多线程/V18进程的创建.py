# 多线程包
import multiprocessing
from time import sleep, ctime

def clock(interval):
    while True :
        print ("The time is %s" % ctime())
        sleep(interval)

if __name__ == '__main__':
    # 启动一个进程
    p = multiprocessing.Process(target=clock, args=(5, ))
    p.start()


