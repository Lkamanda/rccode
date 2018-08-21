import random
import math
class Game_num():
    def line():
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

    def num_game(total,source):
        while
