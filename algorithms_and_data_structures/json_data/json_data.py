import json
import random
import matplotlib.pyplot as plt

x = [random.random() for a in range(10)]
y = [random.random() for b in range(10)]

obj = {
    'x': x,
    'y': y
}

json_obj = json.dumps(obj, indent=4)

with open('sample.json', 'w') as outfile:
    outfile.write(json_obj)

with open('sample.json', 'r') as outfile:
    loaded_json = json.load(outfile)

new_data = loaded_json['x'] + loaded_json['y']

for i in range(0, len(new_data) - 1):
    for j in range(len(new_data) - 1):
        if new_data[j] > new_data[j + 1]:
            num = new_data[j]
            new_data[j] = new_data[j + 1]
            new_data[j + 1] = num

plt.plot(new_data)
plt.show()
