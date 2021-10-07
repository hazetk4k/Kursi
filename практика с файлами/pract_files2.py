with open('byron.txt') as my_file:
    list1 = []
    while True:
        line = my_file.readline()
        if not line:
            break
        list1.append(line.split())
print(list1)
max1 = ""
n = 0
for i in list1:
    while n < len(i):
        if i[n] >= max1:
            max1 = i[n]
        else:
            continue
print(max1)
