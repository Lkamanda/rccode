import pymysql

db = pymysql.connect()
cursor = db.cursor()
cursor.excute('select * from ceshi')

# 查询所有数据
data = cursor.fetchall()