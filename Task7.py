# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input("Введите предельное значение: "))
i = 1
tow_pow = 0
while tow_pow < n:
    tow_pow = 2 ** i
    i += 1
    if tow_pow <= n:
        print(tow_pow)