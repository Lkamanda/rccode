import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', db='db_ceshi', port=3306)

cursor = db.cursor()

# sql更新语句

sql="UPDATE db_admain SET age=age+ce1 WHere username='%s'"%('xiaolin')
try:
    # 数据库提交命令
    cursor.execute(sql)
    db.commit()
    print('提交完成')
except:
    db.rollback()
db.close()