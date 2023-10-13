# Создайте ссылку на пользователя telegram, используя данные из json файла.
# (Подсказка, ссылка состоит из t.me/ и имени пользователя)

# Файл - https://drive.google.com/file/d/1lwgwWAz1OU-JxzqdnTfXZzCVT60h-hJJ/view?usp=sharing
import json

with open('/Users/sergo/Downloads/tme.json', 'r') as f:
    new_list = f.read()
    nickname = json.loads(new_list)['from_user']['username']
    print(f'https://t.me/{nickname}')
