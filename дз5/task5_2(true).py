num = input("Введите число: ")
while not num.isdigit():
    num = input("Введите число: ")
c = 0
flag = 0
i = 1
while c != len(num):
    if num[c] in (num[0:c] +num[c+1:]):
        flag = 1
    c += 1
if flag == 1:
    print('Есть повторяющиеся цифры')
else:
    print('Нет повторяющихся цифр')
