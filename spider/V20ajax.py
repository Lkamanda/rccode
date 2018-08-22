'''
爬取豆瓣电影数据
了解ajax
'''
from urllib import request
import json
import pickle
# ajxa 返回值一般都是json格式
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'
# https://movie.douban.com/j/chart/top_list?type=11
# 正常的网址和类型
#　interval_id=100%3A90  : 打分区间
#  start　＝　　　：从哪开始
#　limit =20　　　：　每次取多少个

rsp = request.urlopen(url=url)
# data 返回值
data = rsp.read().decode()
data = json.loads(data)
# print(data)

# 写入文件

# with open(filename ,'w') as f:
#     f.write(i)
# with open('filename','ab+') as f:
#     pickle.dump(data,f)

# # 读取文件
# with open('filename','rb') as d:
#     db = pickle.load(d)
# print(db)
#
# 把文件以json格式写入文件
filename =r'/home/tlxy/python/rccode/spliderexe/htmlcf/2.json'
with open(filename,'w') as f:
    json.dump(data,f)
print(data)
