import mysql.connector

mydb = mysql.connector.connect(option_files='my.conf')
my_cursor = mydb.cursor()

# 1.
sql = 'SELECT * FROM customers'

my_cursor.execute(sql)

db_result = my_cursor.fetchall()

for row in db_result:
    print(row)

# 2.
sql = 'select name from customers'
my_cursor.execute(sql)

db_result = my_cursor.fetchall()
for row in db_result:
    print(row)

# 3.
sql = "select * from customers"
my_cursor.execute(sql)

first_row = my_cursor.fetchone()

print(first_row)

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name('aridon ', ' krasniqi'))
