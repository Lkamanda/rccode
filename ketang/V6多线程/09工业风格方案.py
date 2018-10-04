import threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        '''

        :param nloops: loop 函数名称
        :param nsec: 系休眠时间
        :return:
        '''
        print('Start loop ', nloop,'at',ctime())
        sleep(nsec)
        print('done loop',nloop,'at',ctime())

    def main(self):
        print("Starting at:",ctime())

        # ThreadFunc("loop").loop 跟以下俩个式子相等
        # t = ThreadFunc("lopp')
        # t.loop
        # 以下式t1,t2的定义方式相等
        t = ThreadFunc("loop")
        t1 = threading.Thread(target = t.loop, args=('loop1', 4))
        t2 = threading.Thread(target = ThreadFunc("loop").loop, args=("LOOP2", 2))

        # 常见错误写法
        # t1 = threading.Thread(target=ThreadFunc('loop').loop(100, 4)
        # t2 = threading.Thread(target=ThreadFunc('loop').loop(100, 2)

        t1.start()
        t2.start()

        # 等待子线程结束或主线程结合素
        t1.join()
        t2.join()

        print('All done at',ctime())

