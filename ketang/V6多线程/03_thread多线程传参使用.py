# 多线程传参
# 利用多线程调用
# 计算总运行时间
# 联系待参数的多线程方法

import time
import _thread as thread

def loop1(in1):
    print ('Start loop 1 ast :', time.ctime())
    print('i am 参数',in1)
    time.sleep(4)
    print('End loop 2 at :',time.ctime())

def loop2(in1,in2):
    print ('Start loop 2 ast :', time.ctime())
    print('i am 参数',in1, in2)
    time.sleep(4)
    print('End loop 2 at :',time.ctime())

def main():
    print ("Starting at:", time.ctime())

    # 元组如果只有一个元素元素后加逗号
    thread.start_new_thread(loop1,("小林",))

    thread.start_new_thread(loop2,("小林","kamanda"))

    print ("ALL DONE AT", time.ctime)

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
