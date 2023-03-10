# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел
# S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

total = int(input("Введите сумму двух чисел: "))
product = int(input("Введите произведение этих же чисел: "))
from math import sqrt
def calculate(total, product):
    D = total*total - 4*product  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        x1 = int((total - sqrt(D))/2)
        x2 = int((total + sqrt(D))/2)
        return [x1, x2]
    elif D == 0:     # если дискриминант = 0 - один корень
        x = int(total/2)
        return [x]
    else:
        print("Решений нет")
print(f"Загаданые числа: {calculate(total, product)}")