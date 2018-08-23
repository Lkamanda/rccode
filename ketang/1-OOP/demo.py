# import math
# a = 5
# print(a/10)
# # 地板除 类似于数学模块当中floor() 向下取整操作
# print(a//10)
# print(a %10)
# b =53
# print(b/10)
# print(b//10)
# print(b%10)
#
# c = 253
# print(c/10)
# print(c//100)
# print(c%10)
# print(c%100)
#
# # 三位数为 xyz
# # 求百位 用 xyz//100
# # 求十位用 先用   xyz％１００　得到  zy ,zy //10 得到 z
# # 求个位 zy % 10得到 y
#
# c=math.floor(985)
# print(c)

# ASCII码转数字
# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))
#
# # 数字转asc码
# print(chr(97))


import random
num = input ('输入123三个数字:')
random_num =random.randrange(1,4)
num = int(num)
rand_num= int(random_num)

if num >rand_num:
    print('输入大了')
elif num == random_num:
    print('相等')
else:
    print('小了')