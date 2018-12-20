import pymsql
db = pymysql('ip地址','数据库用户名'.'密码','连接数据库名')
# 创建游标对象
cursor = db.cursor()
sql = 'insert into 数据库名(FIST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES("liu","dana","18",'M',"1111"),('zhou','jl','19','M','11111')'

# 为了防止sql注入
sql = "INSERT INTO SHUJULUMING(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)VALUES('%s','%s','%d','%c','%s')"% ('liu','dana','18',\'m\',\'10000\')
# 占位符 %s 字符型 , 数值型 %d
try:
    course.excute(sql)
    # 提交执行
    db.commit()
except:
    # 执行失败
    # 回滚
    db.rollback()
db.close()