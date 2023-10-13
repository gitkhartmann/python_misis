# Вывести строку на которой есть слово “салфеткой”

# Файл - https://drive.google.com/file/d/1MMxmUZLHwRhFkcdKN8DV4szUc7nGc1oB/view?usp=sharing


with open('/Users/sergo/Downloads/gogol.txt', 'r') as f:
    new_list = f.read().split('\n')
    for i in new_list:
        if 'салфеткой' in i:
            print(i)
