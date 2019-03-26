import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', db='db_ceshi',port=3306)

cursor = db.cursor()
cursor.execute('show tables')
datas = cursor.fetchall()


# cursor.excute('select *')
# datas = cursor.fetchall()
for data in datas:
   print(data)
# cursor.close()
# except Exception as e:
#     print("查询失败")
# 查询所有数据
'''
fetchall():接受全部返回结果
fetchone():获取下一个结果集
rowcount:只读属性，返回执行语句的影响函数
'''