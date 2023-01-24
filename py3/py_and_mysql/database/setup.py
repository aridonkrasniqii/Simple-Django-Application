import mysql.connector
from database import cursor, db
from mysql.connector import errorcode


DB_NAME = 'dump'

TABLES = {}


TABLES['logs'] = """
    create table logs (
        id int primary key auto_increment not null,
        text varchar(255) not null,
        user varchar(255) not null ,
        created datetime default CURRENT_TIMESTAMP
    )
"""
TABLES['user'] = """
    create table user(
        id int primary key auto_increment,
        user varchar(255) not null,
        password varchar(255) not null
    )
"""
TABLES['deleted'] = """
    create table deleted_user(
        id int primary key auto_increment,
        user_id integer not null,
        user varchar(255) not null,
        password varchar(255) not null
    )
"""


def create_database():
    sql = 'create database if not exists {}'.format(DB_NAME)
    cursor.execute(sql)
    db.commit()
    print(f'Database {DB_NAME} is created')


create_database()


def create_tables():
    for table_name in TABLES:
        try:
            # first use the database
            cursor.execute('use {}'.format(DB_NAME))
            cursor.execute(TABLES.get(table_name))
            db.commit()
            print(f'Table {table_name} is created!')
        except Exception:
            print("Table is not created")


# create_tables()

def create_trigger():
    sql = """
        CREATE TRIGGER before_delete_users
        BEFORE DELETE ON user FOR EACH ROW
        BEGIN
            INSERT INTO deleted_user (user_id, user, password)
            VALUES(OLD.id, OLD.user, OLD.password);
        END
    """

    cursor.execute(sql)
    db.commit()
    print('Trigger is created')


create_trigger()
