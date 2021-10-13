# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def sign_div(n1, n2):
    if n2 == 0:
        print("На ноль делить нельзя!")
        return "Error"
    else:
        return n1 / n2


def sign_plus(n1, n2):
    return n1 + n2


def sign_minus(n1, n2):
    return n1 - n2


def sign_multiple(n1, n2):
    return n1 * n2


num1 = 0
num2 = 0
rez = ""
while 1:
    try:
        num1 = int(input("Введите число 1: "))
    except ValueError:
        print("Введите число!")
        continue
    else:
        break
list_of_signs = ["/", "*", "-", "+"]
sign = input("Введите знак: ")
while not sign in list_of_signs:
    sign = input("Введите знак: ")

while 1:
    try:
        num2 = int(input("Введите число 1: "))
    except ValueError:
        print("Введите число!")
        continue
    else:
        break
if sign == "/":
    rez = sign_div(int(num1), int(num2))
elif sign == "+":
    rez = sign_plus(int(num1), int(num2))
elif sign == "-":
    rez = sign_minus(int(num1), int(num2))
elif sign == "*":
    rez = sign_multiple(int(num1), int(num2))
print(rez)
