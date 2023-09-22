import random
import matplotlib.pyplot as plt

x = [int(random.random() * 10) for a in range(2)]
y = [int(random.random() * 10) for b in range(2)]

matrix = [x, y]
for k in matrix:
    for i in range(0, len(k) - 1):
        for j in range(len(k) - 1):
            if k[j] < k[j + 1]:
                num = k[j + 1]
                k[j + 1] = k[j]
                k[j] = num

plt.plot(matrix[1], matrix[0])
plt.show()
