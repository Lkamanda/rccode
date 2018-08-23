# 包含一个学生类,
# 一个sayhello
# 一个打印语句

class Student():
    def __init__(self, name='NoName', age = 18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {}'.format(self.name))


def sayHello():
    print('WELCOME')

# 尽量不这样使用,明知要一导入我这个模块,就执行这个操作\
print('我是模块p01呀,需要我做什么')