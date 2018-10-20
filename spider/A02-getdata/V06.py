'''
中文unicode案例
'''
import re
hello =u"你好世界"
pattern = re.compile(r'[\u4e00-\u9f5a5]+')
m = pattern.findall(hello)
print(m)