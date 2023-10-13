# Вывести количество запятых в файле

# Файл - https://drive.google.com/file/d/1MMxmUZLHwRhFkcdKN8DV4szUc7nGc1oB/view?usp=sharing


with open('/Users/sergo/Downloads/gogol.txt', 'r') as f:
    new_list = f.read()
    print(new_list.count(','))
