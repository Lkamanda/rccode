'''
内置函数的使用
getattr: 根据字符串的形式去某个模块中寻找东西
hasattr: 根据字符串的形式去某个模块中判断东西是否存在
setattr: 根据字符串的形式去某个模块设置东西
delattr: 删除
'''

from 自动化.note2.login import *
from 自动化.note2.second import *

f = getattr(login, 'logout')
f = getattr()
