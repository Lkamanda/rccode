
'''
调用模块 p01
'''

import p01

stu = p01.Student("xiaolin",22)
stu.say()
p01.sayHello()


print ('*'*10)



# 对命名错误的包借助于工具 importlib 导入
import importlib

# 相当于导入一个包为01 的包,并把导入的模块赋值给了xiaolin
xiaolin = importlib.import_module('01')

stu1 = xiaolin.Student('kaka',25)
stu1.say()
xiaolin.sayHello()


from p01 import Student
stu2 = Student()
stu2.say()