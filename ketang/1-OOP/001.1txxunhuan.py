while 1 :
  def s_juxing():
    for i in range(1,5):
      for j in range(1,6):
        print('*', end=' ')
      print()

  # 空心矩形
  def k_juxing():
    for i in range(1,5):
      for j in range(1,6):
        if i==1 or i==4 or j==1 or j==5:
          print('*', end=' ')
        else:
          print(' ', end=' ')
      print()

  # 实心直角
  def s_zhijiao():
    for i in range(1,6):
      for j in range(6-i,6):
        print('*', end=' ')
      print()


  #空心直角三角形靠左
  def k_zhijiao():
    for i in range(1,6):
      for j in range(6-i,6):
        if j==5 or i==5 or j==6-i:
          print('*', end=' ')
        else:
          print(' ', end=' ')
      print()

  # 实心三角居中
  def s_jzsanjiao():
    for i in range(1,6):
      for m in range(6-i):
        print(end=" ")
      for j in range(6-i,6):
        print("*", end=' ')
      print()
  sjx = ['实心正三角形','实心直角靠左三角形','空心直角三角形','三角形','三角','直角三角形','空心靠左直角三角形']
  sjx_sz = ['实心正直角三角形','三角形','三角','直角三角形']
  sjx_kzz = ['空心正直角三角形','三角形','三角','直角三角形']
  sjx_kzr = ['空心靠左直角三角形','三角形','三角','直角三角形']
  print('输入-1程序结束')
  sr = input ('请输入你想得到的图形：')
  if sr == '-1':
    break
  elif sr in '矩形':
    s_juxing()
    k_juxing()
  elif sr in sjx:
    if sr in sjx_sz:
      s_jzsanjiao()
    if sr in sjx_kzz:
      s_zhijiao()
    if sr in sjx_kzr:
      k_zhijiao()

  else:
    print('你输入的有误')
