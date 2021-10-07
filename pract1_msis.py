# 25. Ввести массивы X(6) и Y(6).В массиве X заменить значения тех элементов Xi, для которых выполняется условие
# |xi - yi| <= 10 значениями элементов Yi.Вывести исходные и результирующий массивы.
import math

from array import *

ar_x = array('i')
ar_y = array('i')
ar_x_new = array('i')

print("Ввод массива X:")
i = 0
while i < 6:
    while True:
        try:
            num = int(input(f"Введите элемент {i + 1}: "))
        except ValueError:
            print('Введите число!')
        else:
            break
    ar_x.append(int(num))
    i += 1
list_x = list(ar_x)
print("Массив X: ", list_x)
print("==========================================================================")
print("Ввод массива Y:")
i = 0
while i < 6:
    while True:
        try:
            num = int(input(f"Введите элемент {i + 1}: "))
        except ValueError:
            print('Введите число')
        else:
            break
    ar_y.append(int(num))
    i += 1
list_y = list(ar_y)
print("Массив Y: ", list_y)
print("==========================================================================")
n = 0
while n < 6:
    if math.fabs(ar_x[n] - ar_y[n]) <= 10:
        ar_x_new.append(ar_y[n])
    else:
        ar_x_new.append(ar_x[n])
    n += 1

list_x_new = list(ar_x_new)
print("Исходыне массивы\nМассив X: ", list_x, "\nМассив Y: ", list_y)
print("Результирующий массив\nМассив X: ", list_x_new)
print("==========================================================================")
