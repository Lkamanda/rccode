import pymysql

conn = pymysql.connect(host='127.0.0.ce1  ', user='root', passwd='5211314zxy.', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages where id =ce1")
print(cur.frtchone())
cur.close()
conn.close()
