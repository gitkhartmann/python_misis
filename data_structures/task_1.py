# Пользователь вводит текст с клавиатуры. Предоставьте пользователю статистику по введенному тексту: количество
# различных слов в нём, количество употреблений каждого из слов в этом тексте.
#
# Примечание. В этой задаче словом можете считать любую последовательность символов, отделенную пробелом от соседних.
#
# Входные данные:
# Одна строка с текстом, которую пользователь вводит с клавиатуры.
#
# Вывод программы:
# В первой строке вывода – количество различных слов в нем в формате «В вашем тексте n различных слов». В последующих
# строках – информация о частотности каждого слова в формате «Слово x встретилось в вашем тексте n раз»
#
# Пример
#
# Входные данные
# текст с повторами слов часто звучит хуже, чем текст без повторов слов
#
# Вывод программы:
# В вашем тексте 10 различных слов
# Слово текст встретилось в вашем тексте 2 раз
# Слово с встретилось в вашем тексте 1 раз
# Слово повторами встретилось в вашем тексте 1 раз
# Слово слов встретилось в вашем тексте 2 раз
# Слово часто встретилось в вашем тексте 1 раз
# Слово звучит встретилось в вашем тексте 1 раз
# Слово хуже, встретилось в вашем тексте 1 раз
# Слово чем встретилось в вашем тексте 1 раз
# Слово без встретилось в вашем тексте 1 раз
# Слово повторов встретилось в вашем тексте 1 раз

import string

phrase = input().translate(
    str.maketrans('', '', string.punctuation)).split()

uniq_words = set(phrase)

print(f'В вашем тексте {len(uniq_words)} различных слов')

for word in uniq_words:
    print(f'Слово {word} встретилось в вашем тексте {phrase.count(word)} раз')