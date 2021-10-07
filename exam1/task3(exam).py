from random import randint
num5 = 0
num6 = 0
count_1 = 0
for i in range(7):
    num1 = int(input('Число 1. >= 1 и <= 20: '))
    while num1 < 1 or num1 > 20:
        num1 = int(input('Число 1. >= 1 и <= 20: '))
    num2 = int(input('Число 2. >= 1 и <= 20: '))
    while num2 < 1 or num2 > 20:
        num2 = int(input('Число 2. >= 1 и <= 20: '))
    num3 = randint(1, 20)
    num4 = randint(1, 20)
    print(num1, num2, '\n', num3, num4)
    if i == 3:
        num5 += num3
        num6 += num4
    if num1 + num2 > num3 + num4:
        count_1 += 1
if count_1 >= 4:
    print(f'Рандомки на 4 итерации: {num5} и {num6}')
print(f'Пара с клавиатуры {count_1} раз оказалась больше')