sept = int(input("Заплати ведьмаку чеканной монетой!\n...Сколько заплатить?: "))
mon = 25
str1 = ""
while mon != 0:
    if sept >= mon:
        str1 += (sept // mon * f"{mon} ")
        if mon == 25:
            sept = sept - (mon * (sept // mon))
            mon = 10
        elif mon == 10:
            sept = sept - (mon * (sept // mon))
            mon = 5
        elif mon == 5:
            sept -= (mon * (sept // mon))
            mon = 1
            continue
        if mon == 1:
            mon = 0
    elif sept < mon:
        if mon == 25:
            mon = 10
        elif mon == 10:
            mon = 5
        elif mon == 5:
            mon = 1
            continue
        if mon == 1:
            mon = 0
print("Могу заплатить вот так:", str1)
