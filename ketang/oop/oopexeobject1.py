import random
import math
n = 0
class Game_num():
    # def __init__(self):
    #     self.n = 0
    def line(self):
        str_num =''
        for i in range(4):
            # ord() 查看asc码
            num = random.randrange(97,123)
            # 把数字转换成asc码形式
            str_s = chr(num)
            str_num  = str_num + str_s
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num +str(num)
            return str_num

    def num_game(self):
        global n
        num = input('shu:')

        str_num = Game_num.line(self)
        random_num = random.randrange(100, 1000)
        if num == '-1' :
            print('不玩了,退出')


        elif num.isdigit() and 100<= int(num)<=999:
            num = int(num)
            random_num = int(random_num)

            if num > random_num:
                print('大了')

            elif num == random_num:
                print('相等了')
            else:
                print('小了')
            return  Game_num.num_game(self)
        else:
            n += 1
            print('您已经输入错误{0}次了'.format(n))
            if n >3:
                print('机会用尽')
                return False
            else:
                return Game_num.num_game(self)

if __name__ == '__main__':

    a = Game_num()
    a.num_game()