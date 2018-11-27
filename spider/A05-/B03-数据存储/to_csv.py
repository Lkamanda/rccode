'''
csv()逗号分隔符，字符分隔符’
csv是由任意的数据记录组成，记录间由某种换行符进行分隔，
ID,UserName,Age,Country
1001,xiaolin,22,China
1002,xiaojun,23,Canada
csv可以使用excal 表格直接打开
'''
import csv
headers = ['ID', 'UserName', 'Age', 'Country']
rows = [
    (1001, 'xiaolin', '22', 'China'),
    (1002, 'xiaojun', '23', 'Canada'),
    (1003, '周佳霖', '30', 'USA')
]
# newline=''去掉换行，
with open('test.csv', 'w', newline='', encoding='utf-8-sig') as f:
    # 生成csv 实例对象
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)