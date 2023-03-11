# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет
# на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число
# ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
# система автоматического сбора черники. Эта система состоит из управляющего
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого
# куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.


print("Введите колличество ягод на каждом кусту через пробел:")
mult_berry = [int(x) for x in input().split()]
res_berry = []
# Создаем списко с суммами трех соседних кустов
for i in range(len(mult_berry) - 1):
    res_berry.append(mult_berry[i - 1] + mult_berry[i] + mult_berry[i + 1])
# Последняя,которая не посчиталась в цикле
res_berry.append(mult_berry[-2] + mult_berry[-1] + mult_berry[0])
print(f"Максимальное кол-во ягод за один заход: {max(res_berry)}")