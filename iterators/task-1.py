# Напишите генератор последовательности чисел трибоначчи tribonacci(n).
#
# n -- натуральное число, индекс последнего элемента в генерируемой последовательности.
#
# Числа трибоначчи – последовательность чисел, отличающаяся от чисел Фибоначчи тем, что следующее число образуется
# как сумма трех предыдущих чисел. Нулевой и первый член последовательности равны 0, второй член последовательности
# равен 1. Начало этой последовательности выглядит так: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274.
#
# Примеры.
#
# list(tribonacci(3)) -> [0, 0, 1, 1] # сгенерировано 4 элемента, так как нумерация элементов последовательности
# трибоначчи с нуля
#
# list(tribonacci(7)) -> [0, 0, 1, 1, 2, 4, 7, 13]

def tribonacci(n):
    a, b, c = 0, 0, 1
    for _ in range(n + 1):
        yield a
        a, b, c = b, c, a + b + c


print(list(tribonacci(3)))