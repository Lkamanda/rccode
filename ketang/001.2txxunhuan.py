from tuxinggonju import Tuxing

# import sys
# sys.path.append(r'/home/tlxy/PCm/pycharm-community-2018.2/rccode/ketang/tuxinggonju.py')
# import Tuxing


c = Tuxing()
a = input('请输入你想的得到的图形名：')
print('当你输入-1时程序结束')
while 1:
  if c == '-1':
    break

  elif c == '矩形':
      c.k_juxing()
      c.s_juxing()
  elif a== '三角形':
    c.k_zhijiao()
    c.s_zhijiao()
    c.s_jzsanjiao()
  else:
    print('请重新输入')






