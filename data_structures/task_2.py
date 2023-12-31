# Часто на практике возникает задача определить уникальность текста. В этом задании вам необходимо подсказать
# пользователю, насколько его текст уникален по сравнению с текстом-образцом. Уникальность будем определять,
# как процентное отношение количества различных слов, которые встречаются в тексте пользователя, но не встречаются в
# тексте-образце, к общему количеству различных слов в тексте пользователя.
#
# Примечание. В этой задаче словом можете считать любую последовательность символов, отделенную пробелом от соседних.
#
# Входные данные:
# Две строки с текстами, каждая вводится с клавиатуры на отдельной строке. В строках не содержится знаков препинания.
# Первая строка – текст-образец. Вторая строка – текст, который надо проверить на уникальность.
#
# Вывод программы:
# В первой строке вывода – информация о количестве общих слов в тексте-образце и тексте пользователя. Во второй строке
# – уникальность, задана как в условии задачи, измеряется в процентах.
# Уникальность требуется округлить до целого значения.
#
# Пример
#
# Входные данные:
# это текст образец текст состоит из некоторого количества слов
# текст с повторами слов часто звучит хуже чем текст без повторов слов
#
# Вывод программы:
# 2
# 80%
#
# Примечание: здесь в тексте-образце и в тексте пользователя два общих слова – «текст» и «слов».
# Общее количество различных слов во втором предложении – 10, поэтому уникальность – 80%.

sample = set(input().split())
text_compare = set(input().split())

print(len(sample & text_compare))
print(f'{int((len(text_compare - sample) / len(text_compare)) * 100)}%')
