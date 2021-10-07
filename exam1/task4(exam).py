import random

kol = int(input('Кол-во: '))
isk = int(input('Искомая: '))
sp_chisel = ''
count = 0
while kol != 0:
    cif = random.randint(1, 100)
    if str(isk) in str(cif):
        count += 1
    sp_chisel += str(cif) + " "
    kol -= 1
print('Рандомные числа: ',sp_chisel)
print(f'Количество встреч цифры {isk} в числах: {count}')

