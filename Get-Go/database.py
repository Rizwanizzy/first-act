import pymysql

con = pymysql.connect(host='localhost', user='root', password='Rizzz', database='study')
cur = con.cursor()

print("teachers details collection")
print("============================")
name = input("enter name:")
age = int(input("enter age:"))
place = input("enter place:")

cur.execute("insert into teacher values(%s,%s,%s)", (name, age, place))

con.commit()
con.close()
