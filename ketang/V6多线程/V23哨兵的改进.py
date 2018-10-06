import multiprocessing
from time import ctime

# 上设置哨兵问题
# 消费者 加入
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    # 此句执行完成,再转入主进程
    print("Out of consumer:", ctime())

def producer(sequence, output_q):
    print("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q" )
    print("Out of producer:", ctime())

if __name__ == '__main__':
    # 创建子进程
    q = multiprocessing.Queue()
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()

    sequence =[1,2,3,4]
    producer(sequence, q)

    # 有几个子线程放几个哨兵 ,可以是None,也可以是其他自定义字符串
    q.put(None)
    q.put(None)
    cons_p1.join()
    cons_p2.join()


