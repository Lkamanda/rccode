import time

# 实现sum（1-100）
def gs(n):
    start = time.perf_counter()
    sum = (n+1)*n/2
    end = time.perf_counter()
    print(end - start)
    return end-start
def sum(n):
    start = time.perf_counter()
    sum = 0
    for i in range(0,n):
        i += 1
        sum += i
    end = time.perf_counter()
    print(end-start)
    return end-start
print(gs(10000000)-sum(10000000))
