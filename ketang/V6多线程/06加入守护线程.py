import time
import threading
def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")
print("main thread ")
t1 = threading.Thread(target=fun, args=())
# 社会守护线程的方法,必须在start之前设置,否则无效

t1.setDaemon(True)
t1.start()
time.sleep(1)

print('main结束')

# 主线程结束后子线程kill