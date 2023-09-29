# !Найдите второй максимум и второй минимум в последовательности чисел.
# Гарантируется, что все числа в последовательности различны, и что в последовательности не менее двух чисел.
# При решении задачи запрещено использовать сортировку списка – обрабатывайте числа потоково, не сохраняя их в список.
#
# Примечание. Пусть numbers – отсортированный по возрастанию список чисел. Тогда второй минимум – элемент с индексом 1,
# второй максимум – элемент с индексом len(numbers) - 1.
#
# Входные данные: целые положительные числа, вводятся по одному в каждой строке. В качестве символа окончания
# последовательности вводится число 0.
#
# Вывод программы: два числа, по одному в каждой строке. Первое – второй минимум среди элементов введенной
# последовательности, второе – второй максимум.
#
# Пример
# Входные данные:
# 1
# 9
# 2
# 5
# 0
#
# Вывод программы:
# 2
# 5
#
# Входные данные:
# 10
# 2
# 0
#
# Вывод программы:
# 10
# 2

a = int(input())
b = int(input())

max_1, min_1 = max(a, b), min(a, b)

max_2, min_2 = 0, 0

while a != 0 and b != 0:
    c = int(input())

    if c == 0:
        if max_2 and min_2:
            print(min_2, max_2)
        else:
            print(min_1, max_1)
        break

    if c > max_1:
        max_2, max_1 = max_1, c
    elif c < min_1:
        min_2, min_1 = min_1, c
    elif min_2 and min_1 < c < min_2:
        min_2 = c
    elif max_2 and max_2 < c < max_1:
        max_2 = c
    elif min_1 < c < max_1:
        if min_2 == 0 and max_2 == 0:
            min_2 = c
        elif min_2 < c > max_2:
            max_2 = c
