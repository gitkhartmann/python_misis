# Подсчитать сумму всех чисел в таблице number
#
# Файл - https://drive.google.com/file/d/1HEPRSz5buwkbmmU3gBGLoVLf4b6Fdyn0/view?usp=sharing

import psycopg2

try:
    conn = psycopg2.connect(database='lesson5_db', user='sergo', password='197612', host='localhost', port='5432')

    cursor = conn.cursor()

    cursor.execute("SELECT num FROM number;")

    data = cursor.fetchall()

    print(sum(n for n, in data))

except:
    print('Can`t connection to database')
