text_file = open('text.txt', 'r')
text = text_file.read()
text = text.lower()

words = text.split()
words = [word.strip('.,!;()[]0123456789') for word in words]

unique = []
for word in words:
    if word and word not in unique:
        unique.append(word)

new_arr = [' '.join(unique[i:i + 10]) for i in range(0, len(unique), 10)]

new_text_file = open('new_text.txt', 'w')

for item in new_arr:
    new_text_file.write("%s\n" % item)
