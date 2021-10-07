num = input("Введите целое положительное число < 10: ")
if num.isdigit() and int(num) < 10:
    for i in range(3):
        print((num + " ") * int(num))
else:
    print("Ошибка! Вы должны ввести целое положительное число < 10!")
    