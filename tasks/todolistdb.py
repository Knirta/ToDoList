import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Install_new!", db="todolist")

cursor = db.cursor()

sql = "INSERT INTO users(fname, lname, login) VALUE ('Alan', 'Harland', 'aharl')"

try:
    cursor.execute(sql)
    db.commit()
except:
    print "error"
    db.rollback()

sql = "select * from users"
cursor.execute(sql)

result = cursor.fetchall()

for rows in result:
    print rows


db.close()
