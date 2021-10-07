num = input("Введите целое число: ")
if num.isdigit():
    print(float(num) ** 3)
else:
    print("Нет, так не работает! Нужно ввести целое число!")
