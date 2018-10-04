import time
import threading
def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")
print("main thread ")
t1 = threading.Thread(target=fun, args=())
t1.start()
time.sleep(1)

print('main结束')
