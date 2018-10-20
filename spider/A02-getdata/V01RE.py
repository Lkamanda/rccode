'''
使用步骤
1,compile 讲正则表达式的字符串编译为一个pattern 对象
2.通过pattern对象的一系列放大对文本进行匹配,匹配结果是一个Match对象
3.Match对象的方法,对结果进行模拟
'''
import re
# \d表示以数字
# 后面+号表示这个数字可以出现一次或者多次
s = r"\d+"
pattern = re.compile(s)
# match 找一个
m = pattern.match("one12two134three5", 3, 10)
print(m)
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))