# Написать программу, при вводе (Имени, даты рождения или города) вывести все строки в которых есть совпадение по
# одному из признаков. В таблице people Файл -
# https://drive.google.com/file/d/1XtJbF512x3QYygOa8Wn_NaB0nhgxy2OS/view?usp=sharing create table people(name text,
# phone_number text, address text, date_of_birth text, email text, job text, credit_card_number text, ipv4 text,
# url text, company text, user_agent text, country text);


import psycopg2

try:
    class DbManager:

        def __init__(self, user, password, host, database):
            self.connection = psycopg2.connect(user=user, password=password, host=host, database=database)
            self.cursor = self.connection.cursor()

        def select_all_by_parameters(self, name='', date_of_birth='', address='', table_name='people'):
            main_request = f"SELECT * FROM {table_name} WHERE "
            if name:
                main_request += f"name='{name}'"
            if date_of_birth:
                main_request += f"{' or ' if name else ''}date_of_birth='{date_of_birth}'"
            if address:
                main_request += f"{' or ' if name or main_request else ''}address='{address}'"
            self.cursor.execute(
                f"{main_request};")
            return self.cursor.fetchall()


    db = DbManager(user='postgres', password='197612', host='localhost', database='lesson5_db')
    print(db.select_all_by_parameters(name='Joseph Munoz', date_of_birth='1926-07-27'))
except:
    print('Can`t connection to database')
