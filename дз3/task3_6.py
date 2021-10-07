num1 = input("Введите целое число 1: ")
num2 = input("Введите целое число 2: ")
if num1.isdigit() and num2.isdigit():
    print(num1, "плюс", num2, "равно", int(num1)+int(num2))
else:
    print("Нужно ввести целые числа!")
