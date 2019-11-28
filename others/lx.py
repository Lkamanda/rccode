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
#
# def my_func(*args):
#     fs = []
#     for i in range(3):
#         def func(_i = i):
#             return _i * _i
#         fs.append(func)
#     return fs
#
# fs1, fs2, fs3= my_func()
# print(fs1())
# print(fs2())
  # print(fs3())

#
# string = "abc123abc123abc123abc123"
# str = "abc"
# # a = str.capitalize()
# print(string.count(str))
#
#
# a = 'fdsf12'
# print(a.isalpha())

with open(file="read.text", mode="r", encoding="utf-8") as f:
    line_list = f.readlines()
    new_line = []
    for line in line_list:
        line = line.strip('\n')
        line = line.split("|")
        # print(type(line))
        # print(line)
        # string.split(str="", num=string.count(str))
        new_line.append(line)
    print(new_line)

    for line in new_line:

        for i in line:
            if i.isalpha():
                print(i)
                i_list = i.strip()
                print(i_list)
