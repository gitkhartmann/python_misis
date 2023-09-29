import random

import psycopg2


class DbManager:

    def __init__(self, user, password, host, database):
        self.connection = psycopg2.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name):
        self.cursor.execute(f'create table {table_name}(x integer, y integer);')
        self.connection.commit()

    def set_random_data(self, table_name, count_rows=10):
        for i in range(count_rows):
            self.cursor.execute(f'insert into {table_name} values(%s, %s);',
                                (random.random() * 10, random.random() * 10))
        self.connection.commit()

    def select_one(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        return self.cursor.fetchone()

    def select_all(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        return self.cursor.fetchall()

    def select_many(self, table_name, size):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        return self.cursor.fetchmany(size=size)

    def select_all_with_option_column(self, table_name, column_name):
        self.cursor.execute(f'select {column_name} from {table_name};')
        return self.cursor.fetchall()

    def copy_to_file(self, path='', table_name=''):
        with open(path, 'w') as f:
            self.cursor.copy_to(file=f, table=table_name, sep=',')
