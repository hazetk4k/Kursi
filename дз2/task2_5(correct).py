rub = int(input("Введите кол-во рублей: "))
cop = int(input("Введите кол-во копеек: "))
if cop / 100.0 >= 1:
    if (rub + cop // 100) % 10 == 1:
        if (rub + cop // 100) % 10 == 11:
            print(rub + cop // 100, "рублей")
        else:
            print(rub + cop // 100, "рубль")
        if (cop - (cop // 100) * 100) % 10 == 1:
            if (cop - (cop) // 100 * 100) == 11:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейка")
        elif (cop - (cop // 100) * 100) % 10 == 2 or (cop - (cop // 100) * 100) % 10 == 3:
            if (cop - (cop // 100) * 100) >= 11 and cop - (cop // 100) * 100 <= 19:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейки")
        elif (cop - (cop // 100) * 100) % 10 == 4:
            if (cop - (cop // 100) * 100) >= 11 and cop - (cop // 100) * 100 <= 19:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейки")
        else:
            print(cop - (cop // 100) * 100, "копеек")
    elif (rub + cop // 100) % 10 == 2 or (rub + cop // 100) % 10 == 3 or (rub + cop // 100) % 10 == 4:
        if (rub + cop // 100) >= 11 and (rub + cop // 100) <= 19:
            print(rub + cop // 100, "рублей")
        else:
            print(rub + cop // 100, "рубля")
        if (cop - (cop // 100) * 100) % 10 == 1:
            if (cop - (cop) // 100 * 100) == 11:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейка")
        elif (cop - (cop // 100) * 100) % 10 == 2 or (cop - (cop // 100) * 100) % 10 == 3:
            if (cop - (cop // 100) * 100) >= 11 and cop - (cop // 100) * 100 <= 19:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейки")
        elif (cop - (cop // 100) * 100) % 10 == 4:
            if (cop - (cop // 100) * 100) >= 11 and cop - (cop // 100) * 100 <= 19:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейки")
        else:
            print(cop - (cop // 100) * 100, "копеек")
    else:
        print(rub + cop // 100, "рублей")
        if (cop - (cop // 100) * 100) % 10 == 1:
            if (cop - (cop) // 100 * 100) == 11:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейка")
        elif (cop - (cop // 100) * 100) % 10 == 2 or (cop - (cop // 100) * 100) % 10 == 3:
            if (cop - (cop // 100) * 100) >= 11 and cop - (cop // 100) * 100 <= 19:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейки")
        elif (cop - (cop // 100) * 100) % 10 == 4:
            if (cop - (cop // 100) * 100) >= 11 and cop - (cop // 100) * 100 <= 19:
                print(cop - (cop // 100) * 100, "копеек")
            else:
                print(cop - (cop // 100) * 100, "копейки")
        else:
            print(cop - (cop // 100) * 100, "копеек")
else:
    if (rub) % 10 == 1:
        if rub == 11:
            print(rub, "рублей")
        else:
            print(rub, "рубль")
        if (cop) % 10 == 1:
            if cop == 11:
                print(cop, "копеек")
            else:
                print(cop, "копейка")
        elif (cop) % 10 == 2 or (cop) % 10 == 3:
            if cop >= 11 and cop <= 19:
                print(cop, "копеек")
            else:
                print(cop, "копейки")
        elif (cop) % 10 == 4:
            if cop >= 11 and cop <= 19:
                print(cop, "копеек")
            else:
                print(cop, "копейки")
        else:
            print(cop, "копеек")
    elif (rub) % 10 == 2 or (rub) % 10 == 3 or (rub) % 10 == 4:
        if (rub) >= 11 and (rub) <= 19:
            print(rub, "рублей")
        else:
            print(rub, "рубля")
        if (cop) % 10 == 1:
            if cop == 11:
                print(cop, "копеек")
            else:
                print(cop, "копейка")
        elif (cop) % 10 == 2 or (cop) % 10 == 3:
            if cop >= 11 and cop <= 19:
                print(cop, "копеек")
            else:
                print(cop, "копейки")
        elif (cop) % 10 == 4:
            if cop >= 11 and cop <= 19:
                print(cop, "копеек")
            else:
                print(cop, "копейки")
        else:
            print(cop, "копеек")
    else:
        print(rub, "рублей")
        if (cop) % 10 == 1:
            if cop == 11:
                print(cop, "копеек")
            else:
                print(cop, "копеек")
        elif (cop) % 10 == 2 or (cop) % 10 == 3:
            if cop >= 11 and cop <= 19:
                print(cop, "копеек")
            else:
                print(cop, "копейки")
        elif (cop) % 10 == 4:
            if cop >= 11 and cop <= 19:
                print(cop, "копеек")
            else:
                print(cop, "копейки")
        else:
            print(cop, "копеек")
