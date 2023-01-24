import mysql.connector as mysql

db = mysql.connect(option_files='my.conf')

# A cursor is an object which helps to execute the query and fetch the records from the database.
# The cursor plays a very important role in executing the query
my_cursor = db.cursor()

my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
    print(x)

db = mysql.connect(
    host='localhost',
    user='teknikashi',
    database='techies',
    password='netflixforfun'
)

my_cursor = db.cursor()
my_cursor.execute('DROP TABLE customers')
my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS customers(name varchar(100) , address varchar(255))")

my_cursor.execute('SHOW TABLES')

for x in my_cursor:
    print(x)

my_cursor.execute('ALTER TABLE customers add column id integer auto_increment primary key')
