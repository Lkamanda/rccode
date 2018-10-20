'''
findall
'''
import re
pattern = re.compile(r"\d+")
s = pattern.findall("i am 22 and 183 high")
print(s)

s = pattern.finditer("i am 22 and 183 high")
print(type(s))
for i in s:
    print(i.group())