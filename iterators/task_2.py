# Напишите функцию compute_nearest_neighbour(p1, points), которая принимает два аргумента:
#
# p1 -- некоторая выделенная точка на плоскости, кортеж из двух элементов (вещественных чисел, координат точки)
#
# points -- набор точек на плоскости, непустой кортеж, элементы которого -- точки, кортежи из двух элементов (
# вещественных чисел, координат точки)
#
# Функция должна возвращать два кортежа.
#
# Первый -- точка из points, которая ближе всего к p1 по Манхэттенской метрике
#
# Второй -- точка из points, которая ближе всего к p1 по Эвклидовой метрике
#
# Пример
# compute_nearest_neighbour((0, 0), ((1, 5), (3, 4))) -> ((1, 5), (3, 4))
# compute_nearest_neighbour((1, 1), ((2, 2), (5, 4), (2, 1))) -> ((2, 1), (2, 1))
#
# Примечание 1. Запрещено использовать циклы, условный оператор и т.д. Используйте элементы функционального
# программирования.
#
# Примечание 2. В случае, если некоторые две точки из points равноудалены от p1, функция может вернуть любую из них.


from functools import partial


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def compute_nearest_neighbour(p1, points):
    manhattan_func = partial(manhattan_distance, p1)
    euclidean_func = partial(euclidean_distance, p1)
    nearest_manhattan = min(points, key=manhattan_func)
    nearest_euclidean = min(points, key=euclidean_func)
    return nearest_manhattan, nearest_euclidean
