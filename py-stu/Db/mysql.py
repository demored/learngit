#/usr/bin/python

#--coding=utf-8--


'''
python 的mysql操作模块PyMysql
'''

import pymysql

host="localhost"
user="root"
pwd="root"
database="test"

try:
    db = pymysql.connect(host, user, pwd, database)
except Exception as e:
    print(e)

cursor = db.cursor()

#####################查询操作
cursor.execute("select version()")
data = cursor.fetchone()
print(data[0])

sql = "show tables"
cursor.execute(sql)
tables = cursor.fetchall()
print(tables)

sql = "select * from user where id = %d" %(1)
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)
###################插入操作


sql = '''
insert into %s (user_tel,price) values(%s, %f)
'''%("user", "1366666",12.44 )

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()


