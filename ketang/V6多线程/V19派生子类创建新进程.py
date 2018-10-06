import multiprocessing
from  time import ctime, sleep

class ClockProcess(multiprocessing.Process):
    '''
    俩个函数蹩脚重要
    1.init 构造函数
    2.run
    '''

    def __init__(self, interval):
        # 调用父类的构造函数
        super().__init__()

        # 在即的变量定义和初始话
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" %ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()


