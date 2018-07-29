#-*-coding:utf-8-*-
'''
定义一个学生的类,用来形容学生
'''

# 定义一个空的类
class Student():
    #一个
    pass


# 定义一个对象
xiaolin = Student()

class PythonStudent():
    # 用None 给不确定的值赋值
    name = None
    age = 18
    course =  "Python"

    # 需要注意
    # 1.注意层级
    #系统默认一个self 参数

    def doHomework(self):
        print ("I do homework")
        return None
        # 推荐在函数末尾使用return 语句

# 实例化一个叫zxy 的学生,是一个具体的人
zxy = PythonStudent()
zxy.doHomework()
# 注意成员函数调用没有传递进入参数
print(zxy.age)
print(zxy.name)

print(zxy.__dict__)
print(Student.__dict__)


