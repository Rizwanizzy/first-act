import pymysql

conn = pymysql.connect(host='localhost', user='root', password='Rizzz', database='study')
cur = conn.cursor()
cur.execute("select * from teacher")
data = cur.fetchall()
for i in data:
    print(i)
nm = input("enter the name:")
cur.execute("select * from teacher where name=%s", nm)
dt_nm = cur.fetchone()

loc = input("enter the location to update:")
cur.execute("update teacher set place=%s where name=%s", (loc, nm))
conn.commit()
cur.execute("select * from teacher")
data = cur.fetchall()
for i in data:
    print(i)
nm = input("enter the name to delete:")
cur.execute("delete from teacher where name=%s", nm)
conn.commit()
for i in data:
    print(i)
conn.close()
