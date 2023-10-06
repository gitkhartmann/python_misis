import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
from heapq import nlargest, nsmallest
import numpy as np

# plt.plot(x, y)
# plt.scatter(x[mask], y[mask], color='orange', s=40, marker='o')
try:
    conn = psycopg2.connect(database='lesson5_db', user='sergo', password='197612', host='localhost', port='5432')

    cursor = conn.cursor()

    cursor.execute(
        "SELECT timestamp, can_data, speed FROM messages WHERE terminal_id = '433100526928099' limit 200;")

    data = cursor.fetchall()
    t = []
    fuel = []
    s = []

    for i, j, sp in data:
        if j['LLS_0']:
            tm = datetime.utcfromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S')
            t.append(tm)
            s.append(sp if sp else 0)
            fuel.append(j['LLS_0'])

    delta = int((max(fuel) - min(fuel)) / 2) // 100

    coordinats = [[t[fuel.index(i)], i] for i in nsmallest(delta, fuel)]

    plt.plot(t, fuel)
    for x, y in coordinats:
        plt.scatter(x, y)

    plt.ylabel('Заправки')
    plt.show()
except:
    print('Can`t connection to database')
