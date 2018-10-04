import time
import threading

def loop1(in1):
    print('starting loop1 at:', time.ctime())
    print('参数:', in1)
    time.sleep(2)
    print('endding loop1 at:', time.ctime())

def loop2(in1,in2):
    print('starting loop2 at', time.ctime())
    print('参数:', in1, in2)
    time.sleep(4)
    print('ending loop2 at:', time.ctime())

def main():
    print('main多线程开启')

    t1 = threading.Thread(target= loop1, args=("小林",))
    t1.start()

    t2 = threading.Thread(target =loop2, args=("小林","草帽"))
    t2.start()

    # 加入等待
    t1.join()
    t2.join()

    print('线程结束:', time.ctime())
if __name__ == '__main__':
    main()
