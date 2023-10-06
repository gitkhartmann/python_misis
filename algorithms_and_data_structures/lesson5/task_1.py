import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt

try:
    conn = psycopg2.connect(database='lesson5_db', user='sergo', password='197612', host='localhost', port='5432')

    cursor = conn.cursor()

    cursor.execute(
        "SELECT timestamp, speed FROM messages WHERE terminal_id = '433100526907106' AND speed > 0 LIMIT 20;")

    data = cursor.fetchall()

    t = []
    s = []

    for i, j in data:
        tm = datetime.utcfromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S')
        t.append(tm)
        s.append(j)
        if j > 40:
            print(f'Водитель превысил скорость на {j - 40}км/ч! Время фиксации: {tm}')

    plt.plot(t, s)
    plt.ylabel('Cкорость пользователя с id=433100526907106')
    plt.show()
except:
    print('Can`t connection to database')
