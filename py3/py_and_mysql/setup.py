import mysql.connector
from database import cursor
from mysql.connector import errorcode


DB_NAME = 'dump'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) not null auto_increment,"
    " `text` varchar(255) not null, "
    " `user` varchar(255) not null,"
    " `created` datetime not null default CURRENT_TIMESTAMP,"
    " primary key (`id`));"
)

TABLES['user'] = ("""
    create table `user` (
        id int(11) primary key not null auto_increment,
        user varchar(250) not null ,
        password varchar(255) not null
    );
""")


def create_database():

    cursor.execute('create database if not exists {} default character set "utf8"'.format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


def create_tables(table = 'fuckoff'): #
    cursor.execute('use {}'.format(DB_NAME))

    for table_name in TABLES:
        try:
            print("Creating table ({}) ".format(table_name) ,end='')
            cursor.execute(TABLES.get(table_name))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Table already exist')
            else:
                print(err.msg)


create_database() #create
create_tables()



