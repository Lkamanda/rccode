# def fib_recur(n):
#   assert n >= 0, "n > 0"
#   if n <= 1:
#     return n
#   return fib_recur(n-1) + fib_recur(n-2)
#
# for i in range(1, 20):
#     print(fib_recur(i), end=' ')


# def fb(n):
#     for i in range(n+1):
#         a, b = 0, 1
#         for y in range(i):
#             a ,b  = b , a+b
#         print(a)
# fb(20)

# class Teacher():
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def teach(self, name):
#         print('%s 教数学' % name)
#
#     def eat(self):
#         print('吃饭')


# def my_func(*args):
#     fs = []
#     for i in range(3):
#         def func():
#             return i * i
#         fs.append(func)
#     return fs
#
#
# fs1, fs2 = my_func()
#
# print(fs1())
# print(fs2())
# # print(fs3())

def my_func(*args):
    fs = []
    for i in range(3):
        def func(_i = i):
            return _i * _i
        fs.append(func)
    return fs

fs1, fs2, fs3= my_func()
print(fs1())
print(fs2())
print(fs3())