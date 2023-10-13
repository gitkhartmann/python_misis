# Дается некоторое натуральное число. Напишите функцию compute_digits_sum, которая возвращает сумму цифр этого числа.
#
# Внимание: для решения этой задачи нельзя использовать циклы или строки, списки. Воспользуйтесь рекурсией.
#
# Функция принимает один аргумент -- натуральное число.
#
# Функция возвращает одно значение: сумму цифр числа, натуральное число.
#
# Пример
# compute_digits_sum(112) -> 4
# compute_digits_sum(11235) -> 12

def compute_digits_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + compute_digits_sum(num // 10)