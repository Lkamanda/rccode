class Tuxing():
  #矩形
  def s_juxing(self):
    for i in range(1,5):
      for j in range(1,6):
        print('*', end=' ')
      print()

  # 空心矩形
  def k_juxing(self):
    for i in range(1,5):
      for j in range(1,6):
        if i==1 or i==4 or j==1 or j==5:
          print('*', end=' ')
        else:
          print(' ', end=' ')
      print()

  # 实心直角
  def s_zhijiao(self):
    for i in range(1,6):
      for j in range(6-i,6):
        print('*', end=' ')
      print()


  #空心直角三角形靠左
  def k_zhijiao(self):
    for i in range(1,6):
      for j in range(6-i,6):
        if j==5 or i==5 or j==6-i:
          print('*', end=' ')
        else:
          print(' ', end=' ')
      print()

  # 实心三角居中
  def s_jzsanjiao(self):
    for i in range(1,6):
      for m in range(6-i):
        print(end=" ")
      for j in range(6-i,6):
        print("*", end=' ')
      print()




# 当直角三角形下有三个选项的时候任何做：靠左 ， 靠右， 居中
#  输入不正确时设置返回，重新输入，超过几次痴线提示，退出


b = Tuxing()

a = input("请输入你想展示的图形名：")
# 空集合 ，错误提示使用

tuku = {'矩形':b.s_juxing,'空心矩形':b.k_juxing,'实心直角三角形靠左':b.s_zhijiao,'空心直角三角形靠左':b.k_zhijiao,'实心居中三角形':b.s_jzsanjiao}
tishi= tuku.keys

#错误提示调用
def tishi():
  c = []
  c.clear()
  print('请输入以下图形名称：', end='')
  for k,v in tuku.items():
    c.append(k)
  print(c)



def f(a) :
  tuku.get(a,tishi)()
f(a)




#　while 1: 加入死循环
# if a == '-1'
    #break

