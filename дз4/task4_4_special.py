a = int(input("Ввести a: "))
b = int(input("Ввести b: "))
for i in range(a, b + 1):
    flag = 1
    for z in range(2, i):
        if i % z == 0:
            flag = 0
    if flag:
        print(i)
