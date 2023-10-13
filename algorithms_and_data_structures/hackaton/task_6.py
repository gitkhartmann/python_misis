# Посчитать количество людей у которых в почте присутствуют цифры в таблице people

# Файл - https://drive.google.com/file/d/1XtJbF512x3QYygOa8Wn_NaB0nhgxy2OS/view?usp=sharing
# create table people(name text, phone_number text, address text, date_of_birth text, email text, job text, credit_card_number text, ipv4 text, url text, company text, user_agent text, country text);

import psycopg2

try:
    conn = psycopg2.connect(database='lesson5_db', user='sergo', password='197612', host='localhost', port='5432')

    cursor = conn.cursor()

    cursor.execute("SELECT phone_number FROM people;")

    data = cursor.fetchall()

    data = [n for n, in data if n.startswith('+7')]
    print(len(data))

except:
    print('Can`t connection to database')
