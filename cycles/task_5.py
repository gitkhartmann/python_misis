# !Напишите программу, которая выводит фрагмент таблицы умножения для чисел из диапазона [x, y] на числа из диапазона
# [w, z], где x, y, w, z – натуральные числа, не превосходящие 10. Обратите внимание на форматирование вывода,
# ориентируйтесь на пример.
#
# Входные данные: в первой строке вводятся числа x, y, во второй строке ввода – w, z. Числа в строке разделены пробелом.
# Первое из пары чисел гарантированно меньше второго.
#
# Вывод программы: фрагмент таблицы умножения. При этом первая строка и первый столбец – заголовочные, в них содержатся
# сами числа из диапазонов. Числа в рамках каждой строки находятся в ячейках длины 7 с выравниванием по левому краю
# (дополняются слева пробелами до длины в 7 символов).
#
# Пример
# Входные данные:
# 2 5
# 3 6
#
# Вывод программы:


y1, y2 = map(int, input().split())
x1, x2 = map(int, input().split())

result = ''
first_row = ''.ljust(7, ' ')

for i in range(x1, x2 + 1):
    first_row = first_row + str(i).ljust(7, ' ')

result = result + first_row + '\n'

for i in range(y1, y2 + 1):
    new_arr = ''
    new_arr = new_arr + str(i).ljust(7, ' ')
    for j in range(x1, x2 + 1):
        new_arr = new_arr + str(j * i).ljust(7, ' ')

    result = result + new_arr + '\n'

print(result)