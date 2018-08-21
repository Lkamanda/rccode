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
