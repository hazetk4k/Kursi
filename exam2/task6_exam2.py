# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# первом списке, так и во втором.
list1 = [1, 2, 3, 3, 4, 5, 6, 8, 12, 75]
list2 = [1, 2, 4, 8, 6, 12, 75, 89]
set1 = set(list1)
set2 = set(list2)
print(len(set2.intersection(set1)))