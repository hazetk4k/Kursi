num1 = input('Введите 7-значное число: ')
while len(num1) < 7 or len(num1) > 7:
    num1 = input('Введите 7-значное число: ')
count_1 = 0
count_2 = 0
for i in num1:
    if int(i) % 2 == 0:
        count_2 += 1
    else:
        count_1 += 1
if count_1 > count_2:
    proizv_136 = int(num1[0]) * int(num1[2]) * int(num1[5])
    print('Произведение 1 3 6: ', proizv_136)
elif count_1 < count_2:
    sum = 0
    for i in num1:
        sum += int(i)
    print("Сумма: ", sum)
