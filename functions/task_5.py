# Даются некоторые натуральные числа num и d. Напишите функцию is_power, которая возвращает True,
# если число num является точной степенью числа d и False в противном случае.
#
# Число num является точной степенью числа d, если d^x=num для некоторого числа x.
#
# Функция принимает два аргумента, num и d, причем d по умолчанию равно 2.
#
# Функция возвращает одно значение: True или False.
#
# Внимание: для решения этой задачи нельзя использовать операцию возведения в степень или аналогичную функцию.
# Используйте рекурсию.
#
# Пример
# is_power(1024) -> True
# is_power(650, 25) -> False

def is_power(num, d=2):
    if d * d > num:
        return False
    elif d * d == num:
        return True
    else:
        return is_power(num, d * 2)
