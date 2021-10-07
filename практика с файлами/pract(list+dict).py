list1 = ["Повара", "Иванов", "Курочкин", "Пирог", "Павела", "Ткачук"]
for i in list1:
    if i[0] == 'П' and i[-1] == "а":
        print(i)
list2 = []
for i in list1:
    list2.append(i[::-1])
print(list2)
n = 0
dict1 = {}
for i in list1:
    dict1[i] = list2[n]
    n += 1
print(dict1)
n = 0
for i in list2:
    dict1.pop(list1[n])
    dict1[i] = list1[n]
    n += 1
print(dict1)
