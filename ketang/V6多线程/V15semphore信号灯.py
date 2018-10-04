import threading
import time

# 参数定义最多几个线程同时使用资源

semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName()+'get semaphore')
        time.sleep(5)
        semaphore.release()
        print(threading.currentThread().getName()+'realease semaphore')

for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()