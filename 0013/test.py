import sqlite3

cx = sqlite3.connect("D:\\Git\\show-me-the-code\\0013\\test.db")
'''
cx.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")

for t in [(0,10,'abc','YU'),(1,20,'cba','XE')]:
    cx.execute("insert into catalog values(?,?,?,?)",t)
cx.commit()
'''
test=cx.execute("select * from catalog")
print(test.description)
print(test.rowcount)
rows=test.fetchall()

for row in rows:
    print(row)
