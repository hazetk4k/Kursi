num = 0
str1 = input("Введите строку: ")
while str1 != "стоп":
    num += 1
    str1 = input("Введите строку: ")
    if str1 == "хватит" or str1 == "достаточно":
        break
print(num)