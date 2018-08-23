print('我是一个错误命名的包')
class Student():
    def __init__(self, name='NoName', age = 18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {}'.format(self.name))


def sayHello():
    print('WELCOME')

# 尽量不这样使用,明知要一导入我这个模块,就执行这个操作\
