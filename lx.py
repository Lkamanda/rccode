# def fib_recur(n):
#   assert n >= 0, "n > 0"
#   if n <= 1:
#     return n
#   return fib_recur(n-1) + fib_recur(n-2)
#
# for i in range(1, 20):
#     print(fib_recur(i), end=' ')


def fb(n):
    for i in range(n+1):
        a, b = 0, 1
        for y in range(i):
            a ,b  = b , a+b
        print(a)
fb(20)

