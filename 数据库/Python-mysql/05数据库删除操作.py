import pymysql

db = pymysql.connect('localhost','root','root','db_ceshi',3306)
cursor = db.cursor()

# 创建sql语句删除
sql= "DELETE FROM db_admain where username='xiaolin'"

try:
    cursor.execute(sql)
    db.commit()
    print('删除成功')
except:
    db.rollback()
db.close()