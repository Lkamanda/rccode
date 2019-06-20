import multiprocessing
from time import ctime, sleep


# 消费者
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        #处理锁
        item = input_q.get()
        print("pull", item, "out of q") # 此处替换为有用的工作
        input_q.task_done() # 发出信号通知任务完成
    # 此处未执行,因为q.join()收集到四个task_done()信号后,主进程启动
    # 未等到pirnt执行
    print("Out of consumer:", ctime())


# 生产者
def producer(sequence, output_q):
    print("Into produce:",ctime())
    # sequence 里存放的是将来要放到queue中的商品
    for item in sequence:
        output_q.put(item)
        # 每放一次打印一次
        print("put", ctime,"into q")
    print("Out of produce:", ctime())


# 建立进程
if __name__ == '__main__':
    # 使用JoinableQueue() 好处待通知
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target = consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    # 生产多个项,sequence代表要发送给消费者的项序列
    # 在实践中,这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence, q)

    # 等待所有项被处理
    q.join()





