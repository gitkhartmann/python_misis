import csv
import random
import matplotlib.pyplot as plt

x = [int(random.random() * 10) for a in range(10)]
y = [int(random.random() * 10) for b in range(10)]

obj = [x, y]

print('obj', obj)
with open('some_csv_file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(obj)

new_data = []
with open('some_csv_file.csv', 'r') as f:
    new_list = f.read().split('\n')
    for i in new_list:
        new_data += i.split(',')

for i in range(0, len(new_data) - 1):
    for j in range(len(new_data) - 1):
        if new_data[j] < new_data[j + 1]:
            num = new_data[j + 1]
            new_data[j + 1] = new_data[j]
            new_data[j] = num

plt.plot(new_data)
plt.show()
