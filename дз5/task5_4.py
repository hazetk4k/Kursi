sum1 = int(input("У вас на карте следующая сумма: "))
count = 0
b = 1
while sum1 > 0:
    pok = int(input(f"Сумма покупки {b} составила: "))
    if (sum1 - pok) < 0:
        print("\tПокупка не совершена! На карте не хватает средств!\n")
        sum1 -= pok
    else:
        sum1 -= pok
        print(f"\tНа карте осталось {sum1}")
        count += 1
        b += 1
print(f"Все! Закупился как следует.\nОсталось ещё {sum1 + pok}р на карте.\nКупил вещей в кол-ве {count}.")