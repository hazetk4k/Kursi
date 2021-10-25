def credit_card(number):
    count = 1
    num = ""
    for i in number[::-1]:
        if count > 4:
            num += "*"
        else:
            num += i
            count += 1
    return num


enter = input("Введите номер карты:")
while not enter.isdigit() or len(enter) < 16:
    enter = input("Введите номер карты:")
res = credit_card(enter)
for i in res[::-1]:
    print(i, end="")
