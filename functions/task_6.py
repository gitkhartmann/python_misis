# Индекс массы тела (ИМТ, англ. body mass index (BMI)) — величина, позволяющая оценить степень соответствия массы
# человека и его роста и тем самым косвенно судить о том, является ли масса недостаточной, нормальной или избыточной.
# Важен при определении показаний для необходимости лечения.
#
# Напишите функцию, которая выводит данные об ИМТ человека согласно приведенной таблице интерпретации.
#
# Индекс можно подсчитать по следующей формуле (где m -- масса в кг, h -- рост в метрах):
#
# Функция принимает произвольное число аргументов: сначала целое число h -- рост в сантиметрах, затем
# последовательность измерений массы человека за некоторый период, состоящую не менее чем из одного вещественного
# числа. Для расчета ИМТ используется средний вес человека за этот период.
#
# Функция ничего не возвращает, но выводит данные на экран. Обратите внимание на примеры.

def bmi_info(h, *weight):
    dict = {
        1: {
            'classification': 'Underweight',
            'health_risk': 'Minimal'
        },
        2: {
            'classification': 'Normal',
            'health_risk': 'Minimal'
        },
        3: {
            'classification': 'Overweight',
            'health_risk': 'Increased'
        },
        4: {
            'classification': 'Obese',
            'health_risk': 'High'
        },
        5: {
            'classification': 'Severely Obese',
            'health_risk': 'Very High'
        },
        6: {
            'classification': 'Morbidly Obese',
            'health_risk': 'Extremely High'
        },
    }

    bmi = round((sum(weight) / len(weight)) / (h / 100) ** 2, 1)
    idx = int()
    if bmi < 18.5:
        idx = 1
    elif 18.5 <= bmi < 25:
        idx = 2
    elif 25 <= bmi < 30:
        idx = 3
    elif 30 <= bmi < 35:
        idx = 4
    elif 35 <= bmi < 40:
        idx = 5
    elif bmi > 40:
        idx = 6

    key = dict[idx]
    print(f"""
    Your BMI: {bmi}
    It can be classificate as {key['classification']}
    Risk for your health is {key['health_risk']}
    """)


bmi_info(155, 49, 51, 50)
