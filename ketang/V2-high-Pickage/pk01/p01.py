print('我在pk01文件下')
class Student():
    def __init__(self, name='NoName', age = 18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {}'.format(self.name))


def sayHello():
    print('WELCOME to pk01')