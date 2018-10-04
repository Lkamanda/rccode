import threading
import time

def loop1():
    print('start loop1 at :', time.ctime() )
    time.sleep(5)
    print('END loop1 at:' , time.ctime())

def loop2():
    print('START loop2 at:',time.ctime())
    time.sleep(3)
    print('End loop2 at:', time.ctime())

def loop3():
    print('Start loop3 at:', time.ctime())
    time.sleep(4)
    print('End loop3 at :', time.ctime())

def main():
    print("starting at :", time.ctime())
    t1 =threading.Thread(target=loop1, args=())
    # 设置进程名称
    t1.setName("Thread_1")
    t1.start()


    t2 = threading.Thread(target=loop2, args=())
    t2.setName("Thread_2")
    t2.start()


    t3 = threading.Thread(target =loop3, args=())

    t3.setName("Thread_3")
    t3.start()


    time.sleep(3)
    for thr in threading.enumerate():
        print(thr.getName())
    print(threading.activeCount())

    print("all done at :", time.ctime())
if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)