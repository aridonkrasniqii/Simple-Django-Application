import mysql.connector


config = {
    'user': 'teknikashi',
    'password': 'netflixforfun',
    'host': 'localhost',
    'database': 'dump'
}

db = mysql.connector.connect(**config)

cursor = db.cursor()
