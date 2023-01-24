import mysql.connector
from database import db, cursor


def add_log(text, user):
    sql = "insert into logs(text,user) values(%s, %s);"
    cursor.execute(sql, (text, user, ))
    db.commit()
    last_id = cursor.lastrowid
    print("Last inserted is {}".format(last_id))


def get_log():
    sql = 'select * from logs'
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    for row in result:
        print(row, end=' ')


def update_log(id, text):
    sql = 'update logs set text = %s where id = %s'
    cursor.execute(sql, (text, id,))
    db.commit()
    print('Log is updated !')


def delete_log(id):
    sql = 'delete from logs where id = %s'
    cursor.execute(sql, (id, ))
    db.commit()
    print("Log is deleted")


def add_user(user, password):
    sql = 'insert into user(user, password) values(%s , %s)'
    cursor.execute(sql , (user, password, ))
    db.commit()
    last_id = cursor.lastrowid
    print(f'Last inserted is {last_id}')

def get_user():
    pass


def update_user():
    pass

def delete_user(id):
    sql = 'delete from user where id = %s'
    cursor.execute(sql, (id,))
    db.commit()
    print("User is deleted")


add_log('This is the first log ', 'Aridon')
add_user('arid', 'asdasdasd')
delete_user(2)
