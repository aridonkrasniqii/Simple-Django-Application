import mysql.connector

"""
    CONNECTION TO MYSQL USING CONNECTOR/PYTHON

"""

# 1.
db = mysql.connector.connect(
    host='localhost',
    user='teknikashi',
    password='netflixforfun'
)
print("Connection id: ", db.connection_id)

# Instead of passing connection credentials as keyword arguments, you also pass them in a dictionary
# 2.

connection_args = {
    'host': 'localhost',
    'user': 'teknikashi',
    'password': 'netflixforfun'
}
db = mysql.connector.connect(**connection_args)

print('Connection id : ' + str(db.connection_id))

db = mysql.connector.connect(option_files='my.conf')

print('Connection Id : ' + str(db.connection_id))
