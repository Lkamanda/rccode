import pymysql

# import MySQLdb
#
# conn = MySQLdb.connect(host = '×××××××××××××',  # 远程主机的ip地址，
#                                             user = 'root',   # MySQL用户名
#                                             db = 'alimusic',   # database名
#                                             passwd = '××××××',   # 数据库密码
#                                             port = 3306,  #数据库监听端口，默认3306
#                                             charset = "utf8")  #指定utf8编码的连接
# cursor = conn.cursor()  # 创建一个光标，然后通过光标执行sql语句
# cursor.excute("select * from table1 limit 10")
# values = cursor.fetchall()  # 取出cursor得到的数据
# cursor.close(); conn.close()  #最后记得关闭光标和连接，防止数据泄露

try:
    # 获取一个数据库 注意charset ='utf-8'
    # 打开数据库连接
    '''
    host:服务器地址
    user:登录数据库的用户
    password:mysql密码
    db:连接使用的数据库名
    port:端口号,默认3306
    '''
    db = pymysql.connect(host='localhost', user='root', password='zhoujialin123', db='db_ceshi', port='3306')
    print(type(db))
    # 创建游标
    cursor = db.cursor()
    cursor.execute('DROP TABLES IF EXISTS School')
    # 使用预处理创建表
    sql = '''create table School(
    FIRST NAME CHAR(20) NOT NULL,
    LAST NAME CHAR(20)
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)
    '''
    cursor.execute(sql)
    db.close()

except:
    pass
