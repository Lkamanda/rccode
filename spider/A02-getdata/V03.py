'''
search
'''
import re

s = r"\d+"
pattern = re.compile(s)

m = pattern.search("one12two34three56")
print(m.group())
# 参数表明首查

m = pattern.search("one12twoth34ree56", 5, 40)
print(m.group())