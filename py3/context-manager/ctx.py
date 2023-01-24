# ctx.py

from sqlite3 import connect

# with ctx() as x:
#   pass


# x = ctx().__enter__
# try:
#     pass
# finally:
#     x.__exit()__


"""
with connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('create table if not exists points(x int , y int)')
    cur.execute('insert into points(x,y) values(1,1)')
    cur.execute('insert into points(x,y) values(2,2)')
    cur.execute('insert into points(x,y) values(3,3)')
    cur.execute('insert into points(x,y) values(4,4)')
    for row in cur.execute('select * from points'):
        print(row)
    for row in cur.execute('select sum(x * y) from points '):
        print(row)

    cur.execute('drop table points')
"""


class temptable:

    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        print("__enter__")
        self.cur.execute('create table points(x int , y int)')

    def __exit__(self, *args):
        print("__exit__")
        self.cur.execute('drop table points')


with connect('test1.db') as conn:
    cur = conn.cursor()

    with temptable(cur):
        cur.execute('insert into points (x,y) values(1, 2)')
        cur.execute('insert into points (x,y) values(1, 2)')
        cur.execute('insert into points (x,y) values(1, 2)')
        cur.execute('insert into points (x,y) values(1, 2)')

        for row in cur.execute('select * from points '):
            print(row)
        for row in cur.execute('select sum(x * y) from points '):
            print(row)
        # if drops the table at the end
