#file 1 mydb.py
import MySQLdb

class MyDB(object):
    def init(self):
      db = MySQLdb.connect(host="localhost", user="root", passwd="Install_new!", db="todolist")
      cursor = db.cursor()

    def select(self, tuple_tables, kwargs):
      sql = "select * from users"
      columns_str = kwargs.values()
      tab
      cursor.execute(sql)
      result = cursor.fetchall()
      return result
 
   def insert(self, tuple_tables, kwargs_values):
      sql = "INSERT INTO users(fname, lname, login) VALUE ('Alan', 'Harland', 'aharl')"

      try:
        cursor.execute(sql)
        db.commit()
      except:
        print "error"
        db.rollback()

#file 2 lab1.py

from mydb import MyDB

mydb = MyDB()
mydb.init()

result = mydb.select('users','fname')
mydb.insert('users', {'fname' : 'Alan',...}

for rows in result:
    print rows

db.close()

