import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "5211314zxy.", "TESTDB")
# 使用cursor()方法创建一个游标对象
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")

# 使用fetchone() 方法获取单条数据
data = cursor.fetchone()

print("Database version :%s" % data)
# 关闭数据库
db.close()