import psycopg2

# from dbmanager import DbManager

try:
    # c = connectionDB(user='postgres', password='197612', host='localhost', database='air')
    # print(c.select_all())
    # print('OK')
    # print(c.select_many(3))

    conn = psycopg2.connect(database='air', user='postgres', password='197612', host='localhost')

    cursor = conn.cursor()
    cursor.execute('insert into departures values(%s, %s);', ("АЭРОФЛОТ", 6765))
    cursor.execute('insert into departures values(%s, %s);', ("АЭРОФЛОТ", 6765))
    cursor.execute('insert into departures values(%s, %s);', ("АЭРОФЛОТ", 6765))
    cursor.execute('insert into departures values(%s, %s);', ("АЭРОФЛОТ", 6765))
    cursor.execute('insert into departures values(%s, %s);', ("АЭРОФЛОТ", 6765))
    cursor.execute('insert into departures values(%s, %s);', ("АЭРОФЛОТ", 6765))
    conn.commit()
    cursor.execute('SELECT * FROM departures;')

    users = cursor.fetchall()
    print('USERS', users)
except:
    # в случае сбоя подключения будет выведено сообщение
    print('Can`t connection to database')
