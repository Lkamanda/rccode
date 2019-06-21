import random


class Food():
    def __init(self):
        ''' 自动产生一个食物 '''
        self.new_food()

    def new_food(self):
        '''产生一个食物 坐标 随机生成，并且不为蛇当前位置'''
        x = random.randrange()
        self.postion = x, y  # 存放食物位置
