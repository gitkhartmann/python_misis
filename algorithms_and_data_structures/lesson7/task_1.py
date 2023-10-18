a, b = map(int, input().split())
# задача 1 Напишите программу, которая выводит квадратную матрицу размера n на n
mtrx = [[i if i % 2 == 0 else j for j in range(1, b + 1)] for i in range(1, a + 1)]

# задача 2 и 3 Найти максимальное и минимальное число в матрице

values = set()

for k in mtrx:
    values.update(k)

print(max(values))
print(min(values))

# задача 4 и 5 Отсортировать матрицу по убыванию или возрастанию
new_mtrx = []
for m in mtrx:
    new_mtrx += m

for i in range(len(new_mtrx) - 1):
    for j in range(len(new_mtrx) - 1):
        if new_mtrx[j] < new_mtrx[j + 1]:
            new_mtrx[j + 1], new_mtrx[j] = new_mtrx[j], new_mtrx[j + 1]

up_mtrx = []
for e in range(0, len(new_mtrx), b):
    up_mtrx.append(new_mtrx[e: e + b])

# Задача 6 Заполнить матрицу по диагонали справа-сверху слева-вниз
a, b = map(int, input().split())
mtrx = [[None for j in range(1, b + 1)] for i in range(1, a + 1)]

for diag in range(2 * b - 1):
    for i in range(b):
        for j in range(b):
            if i + j == diag:
                mtrx[i][j] = 1

print(mtrx)
