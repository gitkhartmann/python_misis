# Пользователям редко удается придумать достаточно "хороший" пароль. В этом задании вам требуется реализовать
# генерацию "почти" случайных паролей. "Почти" -- потому что за основу необходимо взять пароль, придуманный
# непосредственно пользователем.
#
# На основе введенной пользователем строки сгенерируйте случайный пароль заданной пользователем длины.
#
# В пароле обязательно должны содержаться:
#
# -все символы из пароля, изначально введенного пользователем. Каждый из этих символов в итоговом пароле должен
# повторяться как минимум такое же количество раз, как в изначально введенном и быть в том же регистре.
#
# -как минимум одна буква в верхнем регистре.
# -как минимум одна буква в нижнем регистре.
# -как минимум одна цифра.
#
# Входные данные:
# pass, пароль
# p_len, натуральное число, желаемая длина пароля
# Значения вводятся с клавиатуры в одной строке через пробел.
# Гарантируется, что p_len > len(pass) и что все требования к паролю можно реализовать
#
# Вывод программы:
# Сгенерированный согласно условиям задачи пароль
#
# Пример
# Входные данные:
# qwerty 10
# Вывод программы (один из возможных):
# A7we0t7qry
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice, shuffle, choices


def generate_password(password, p_len):
    missing_len = int(p_len) - len(password)
    low_letters, upp_letters, set_digits = set(ascii_lowercase), set(ascii_uppercase), set(digits)
    set_pass, password = set(password), list(password)

    while missing_len != 0:
        if not len(low_letters & set_pass):
            password += [choice(ascii_lowercase)]
            missing_len -= 1
        if not len(upp_letters & set_pass) and missing_len:
            password += [choice(ascii_uppercase)]
            missing_len -= 1
        if not len(set_digits & set_pass) and missing_len:
            password += [choice(digits)]
            missing_len -= 1
        if missing_len:
            password += choices(ascii_lowercase + ascii_uppercase + digits, k=missing_len)
            missing_len = 0
            shuffle(password)

    return ''.join(password)


password, p_len = input().split()
generate_password(password, p_len)
