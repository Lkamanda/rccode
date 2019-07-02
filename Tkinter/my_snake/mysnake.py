import random

class Food:
    def __init__(self, queue):
       """自动产生一个食物"""
        self.queue = queue
        self.new_food()

    def new_food(self):
        """ 产生一个食物 坐标 随机生成，并且不为蛇当前位置 """
        x = random.randrange(50, 500, 10)
        y = random.randrange(50, 500, 10)
        # 存放食物位置
        self.postion = x,y
        # 消息队列不能随意访问内部元素，只提供从头弹出，从尾部追加， 先进先出
        # 把一个食物产生的消息方入消息队列中，
        # 消息的格式自己定义，
        # 此处定义的是dict . k 代表消息类型，v代表此类型的数据
        self.queue.put({"food":self.postion})

class Snake():
    """
    蛇的功能：
        1.蛇能动，由我们的上下左右建控制
        2.蛇每次动，都需要重新计算蛇头的位置
        3.检查是否游戏完成的功能
    """
    def move(self):
        """
        负责蛇的移动
        1.重新计算蛇头的坐标
        2.当蛇头跟实物相遇（坐标相等）， 通知world 则加分，重新生成食物，
        3.否则，蛇需要动
        """
        new_snake_point = self.cal_new_pos()  # 重新计算蛇头位置

        # 蛇头位置跟实物位置相同时
        if self.food.postion == new_snake_point:
            self.points_earned + = 1 # 得分加1
            self.queue.put({"points_earned": self.points_earned})   # 将消息传入消息队列中
            self.food.new_food()  # 就得实物被吃掉，产生新的实物
        # 当蛇的位置和食物不同时
        else:
            # 需要注意蛇的信息保存方式
            # 在tkinter 中蛇头和蛇尾的存储位置是相反的
            # 每次移动是删除蛇最前的位置,并在后面追加
            self.snake_points.pop(0)
            # 判断程序是否退出，因为新的蛇可能中签
            self.check_game_over(new_snake_point)
            self.snake_poinrs.append(new_snake_point) # 将蛇撞墙的信息传入消息队列

    def cal_new_postion(self):
        """
        计算新的蛇头的位置
        """
        last_x , last_y = self.snake_postions[-1]
        # direction 负责存储蛇的移动的方向
        # 向上移动
        if self.direction == "Up":
            # 每次移动的跨度是10像素
            new_snake_point = last_x, last_y - 10
        elif self.direction == "Down":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Left":
            new_snake_point = last_x -10 , last_y
        elif self.direction == "Right":
            new_snake_point = last_x + 10, last_y

        return new_snake_point


    def check_game_over(self, snake_point):
        """判断的依据是适合有是否和墙相撞"""
        x,y = snake_point[0], snake_point[1]
        if not -5< x <








