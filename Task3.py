# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

num = int(input('Введите число n: '))
print(f'n = {num}; nn = {num*2}; nnn = {num*3}.')
print(f'сумма чисел = {num+num*2+num*3}')