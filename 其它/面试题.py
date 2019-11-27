

# for i in range(5):
#
#     for j in range(5 - i):
#         print(' ', end='')
#
#     for m in range(i + 1):
#         print("* ", end='')
#     print(" ")



# for i in range(1,5):
# #     for k in range(1,7-i):
# #         print(end=' ')
# #     for j in range(6-i,6):
# #         print('*', end=' ')
# #     print()
# # for i in range(1,6):
# #     for k in range(i):
# #         print(end=' ')
# #     for j in range(6-i):
# #         print('*', end=' ')
# #     print()

# for i in range(1,6):
#     # 控制列，规则是第一行五列，第二行是四列  i =1,j的范围6 ，i =2,j=5
#     for j in range(1,7-i):
#         print('*', end="")
#     print()

class Xm:
    def __init__(self):
        self.weight = 75

    def run(self):
        self.weight -= 1

    def eat(self):
        self.weight += 0.5

zjl = Xm()
print(zjl.weight)
zjl.run()
print(zjl.weight)


class House:
    def __init__(self):
        self.chuang = 4
        self.yigui = 2
        self.canzhou = 1.5
        self.chuang_name = "床"
        self.yigui_name = "衣柜"
        self.canzhuo_name = "餐桌"

    def output(self, area, huxing):
        jiaju = []
        area = area - self.chuang - self.yigui - self.canzhou
        jiaju.append(self.chuang_name)
        jiaju.append(self.yigui_name)
        jiaju.append(self.canzhuo_name)
        print("房子：户型:{0},总面积:{1},家具列表：{2}".format(huxing, area,jiaju))


new_house = House()
new_house.output(area=50, huxing="俩室一厅")


class Gun:
    def __init__(self):
        self.danyao_num = 30
        self.name = "ak47"
    def shut(self):
        print('开火')
        self.danyao_num -= 1
    def lodding(self):
        self.danyao_num += 30

class Solid():
    def shuout(self, gun):
        gun.shut()

ak47 = Gun()
rean = Solid()

rean.shuout(gun=ak47)
print(ak47.danyao_num)

