# 7. Напишите программу, демонстрирующую работу try\except\finally
try:
    a = input("Введите делимое: ")
    b = input("Введите делитель: ")
    rez = int(a) / int(b)
except ValueError:
    print("Вы должны ввести цифры!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print(f"Результат: {rez}")
finally:
    print("Что бы не произошло, эта строка появится!")
