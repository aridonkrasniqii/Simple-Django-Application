# crud stuff
from database import cursor, db


def add_log(text, user):
    sql = 'insert into `logs` (text, user) values(%s, %s)'
    cursor.execute(sql , (text, user, ))
    db.commit()
    log_id = cursor.lastrowid
    print('Added log {}'.format(log_id))




def get_logs():
    sql = 'select * from logs order by created DESC'
    cursor.execute(sql)
    result = cursor.fetchall()
    for id , text, user, time in result:
        print(f'id={id}, text={text}, name={user}, time={time}')


def update_logs(id,text):
    sql = 'update `logs` set text = %s where id = %s'
    cursor.execute(sql, (text, id, ))
    db.commit()
    print('Log updated')


update_logs(1, 'Updated log')
get_logs()




# add_log('This is log one ' , 'Brad')
# add_log('This is log two ' , 'Jeff')
# add_log('THis is log three' , 'Jane')



