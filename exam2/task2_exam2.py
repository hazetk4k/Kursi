# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
list1 = [1, 3, 2, 3, 2, 3, 4, 8, 5, 8]
list2 = []
kol_par = 0
for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i)
        if list1.count(i) == 1:
            continue
        else:
            if list1.count(i) == 2:
                kol_par += 1
            elif list1.count(i) > 2:
                kol_par += list1.count(i)
print(f"Количество пар в списке: {kol_par}")
