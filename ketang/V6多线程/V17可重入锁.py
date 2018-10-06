import threading
import time
class Mythread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num = num+1
            msg = self.name+'set num to' + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0

mutex = threading.RLock()

def test1():
    for i in range(5):
        t = Mythread()
        t.start()

if __name__ == '__main__':
    test1()