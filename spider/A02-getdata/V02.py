import re
# 以下正则被分成俩个组,以小口号为单位
s = r'(([a-z]+) ([a-z]+))'
# re.I 表示忽略大小写
pattern = re.compile(s, re.I)
m = pattern.match("Hello world wide web ")
# group(0)表示返回匹配成功的整个子串
s = m.group(0)
print(s)
# 返回匹配成功的整个子串的跨度
a3 = m.span(0)
print(a3)

a1 = m.group(1)
print(a1)
a2 = m.group(3)
print(a2)

a4 = m.groups()
print(a4)
# 返回匹配成功的整个子串的跨度
