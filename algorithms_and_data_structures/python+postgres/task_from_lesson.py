# Выполнить задачи из предыдущего урока, но с использованием python (кроме 4 и 6)
# Создать таблицу в базе данных (x integer, y integer)
# Заполнить таблицу сгенерированными данными (минимум 30 записей)
# (новый файл) Получить данные из таблицы
# Создать два списка (x и y), заполнить их данными из таблицы
# Построить график по полученным данным
# * Отсортировать данные по возрастанию и построить график
# * Отсортировать данные по убыванию и построить график

from dbmanager import DbManager
import matplotlib.pyplot as plt

db = DbManager(user='postgres', password='197612', host='localhost', database='air')
db.create_table(table_name='qas')
db.set_random_data(table_name='qas', count_rows=40)
db.copy_to_file(path='/Users/sergo/Desktop/new3.csv', table_name='qas')

x = [int("".join(c for c in str(num) if c.isdecimal())) for num in
     db.select_all_with_option_column(table_name='qas', column_name='x')]
y = [int("".join(c for c in str(num) if c.isdecimal())) for num in
     db.select_all_with_option_column(table_name='qas', column_name='y')]

plt.plot(x, y)
plt.show()

for j in range(len(x) - 1):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            z = x[i]
            x[i] = x[i + 1]
            x[i + 1] = z

    for i in range(len(y) - 1):
        if y[i] > y[i + 1]:
            z = y[i]
            y[i] = y[i + 1]
            y[i + 1] = z

plt.plot(x, y)
plt.show()

for j in range(len(x) - 1):
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            z = x[i]
            x[i] = x[i + 1]
            x[i + 1] = z

    for i in range(len(y) - 1):
        if y[i] < y[i + 1]:
            z = y[i]
            y[i] = y[i + 1]
            y[i + 1] = z

plt.plot(x, y)
plt.show()
