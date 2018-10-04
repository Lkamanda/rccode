'''
利用times函数,生成俩个函数
程序调用
计算总时间
'''
import  time
import  threading

def loop1():
    # ctime 得到当前时间点
    print ('Start loop 1 at :', time.ctime())
    #  睡眠多长时间,单位是秒
    time.sleep(4)
    print('End loopr 1 at:',time.ctime())

def loop2():
    print('Start loop 2 at:', time.ctime())
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('Starting at :', time.ctime())
    loop1()
    loop2()
    print("ALL DONE at:", time.ctime())
    # 总共时间6秒

if __name__ == '__main__':
    main()