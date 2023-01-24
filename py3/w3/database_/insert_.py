import mysql.connector

db = mysql.connector.connect(option_files='my.conf')
my_cursor = db.cursor()

sql = "insert into customers (name, address) values (%s, %s)"
val = ('John', 'Highway 21')

my_cursor.execute(sql, val)
db.commit()

print(my_cursor.rowcount, ' record inserted. ')

# Insert multiple records


sql = 'insert into customers (name, address ) values (%s, %s)'
val = [('Peter', 'Lowstreet 3'), ('Amy', 'Apple st 652'), ('Michael', 'Valley 345'), ('Sandy', 'Ocean blvd 2 ')]

my_cursor.executemany(sql, val)
db.commit()

print(my_cursor.rowcount, ' rows was inserted ')

""" 
    *** GET LAST INSERTED ID ***
"""

print('1 record inserted , ID = ', my_cursor.lastrowid)
