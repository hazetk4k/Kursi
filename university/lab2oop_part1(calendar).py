class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def change_day(self, new_day):
        list1 = [1, 3, 5, 7, 8, 10, 12]
        list2 = [4, 6, 9, 11]
        if self.month in list1:
            if new_day > 31 or new_day < 1:
                print("В текущем месяце 31 дней!")
                return "Error"
            else:
                self.day = new_day
        elif self.month in list2:
            if new_day > 30 or new_day < 1:
                print("В текущем месяце 30 дней!")
                return "Error"
            else:
                self.day = new_day
        elif self.month == 2:
            if new_day > 28 or new_day < 1:
                print("В текущем месяце 28 дней!")
                return "Error"
            else:
                self.day = new_day

    def change_month(self, new_month):
        list2 = [4, 6, 9, 11]
        if new_month == 2:
            if int(self.day) > 28:
                print("Установленное число не соответствует месяцу!")
                return "Error"
        elif new_month in list2:
            if int(self.day) > 30:
                print("Установленное число не соответствует месяцу!")
                return "Error"
        if new_month > 12 or new_month < 1:
            print("Всего 12 месяцев!")
            return "Error"
        else:
            self.month = new_month

    def change_year(self, new_year):
        if new_year > 3000 or new_year < 1000:
            print("Год должен быть в пределах от 1000 до 3000!")
            return "Error"
        else:
            self.year = new_year

    def show_day(self):
        print("День: ", self.day)

    def show_month(self):
        print("Месяц: ", self.month)

    def show_year(self):
        print("Год: ", self.year)

    def show_f1(self):
        dict1 = {
            1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря",
        }
        mo = dict1[self.month]
        print(f"{self.day} {mo} {self.year} года")

    def show_f2(self):
        print(f"{self.day}.{self.month}.{self.year}")

    def day_one(self):
        list1 = [1, 3, 5, 7, 8, 10, 12]
        list2 = [4, 6, 9, 11]
        self.day = self.day + 1
        if self.month in list1:
            if self.day > 31:
                self.day = 1
                self.month += 1
        elif self.month in list2:
            if self.day > 30:
                self.day = 1
                self.month += 1
        elif self.month == 2:
            if self.year % 400 == 0:
                if self.day > 29:
                    self.day = 1
                    self.month += 1
            else:
                if self.year % 100 == 0:
                    if self.day > 28:
                        self.day = 1
                        self.month += 1
                elif self.year % 4 == 0:
                    if self.day > 29:
                        self.day = 1
                        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1


cal = Calendar(1, 1, 1001)
while True:
    print("===========================================================================================")
    print("1 - установка дня, месяца или года\n2 - получение дня, месяца или года")
    print("3 - Дата в формате 1\n4 - Дата в формате 2\n5 - дата через 24 часа\n6 - выход")
    print("===========================================================================================")
    choice = input("Выберете одну из предложенных операций: ")
    while not choice.isdigit() or int(choice) > 6 or int(choice) < 1:
        choice = input("Выберете одну из предложенных операций: ")
    if int(choice) == 6:
        break
    elif int(choice) == 1:
        print("===========================================================================================")
        print("1 - изменить день\n2 - изменить месяц\n3 - изменить год")
        print("===========================================================================================")
        choice2 = input("Выберете одну из предложенных операций: ")
        while not choice2.isdigit() or int(choice2) > 3 or int(choice2) < 1:
            choice2 = input("Выберете одну из предложенных операций: ")
        if int(choice2) == 1:
            while True:
                d = input('Введите новый день: ')
                while not d.isdigit():
                    d = input('Введите новый день: ')
                if cal.change_day(int(d)) == "Error":
                    continue
                else:
                    cal.change_day(int(d))
                    cal.show_f1()
                    break
        elif int(choice2) == 2:
            while True:
                m = input('Введите новый месяц: ')
                while not m.isdigit():
                    m = input('Введите новый месяц: ')
                if cal.change_month(int(m)) == "Error":
                    continue
                else:
                    cal.change_month(int(m))
                    cal.show_f1()
                    break
        elif int(choice2) == 3:
            while True:
                y = input("Введите новый год: ")
                while not y.isdigit():
                    y = input('Введите новый год: ')
                if cal.change_year(int(y)) == "Error":
                    continue
                else:
                    cal.change_year(int(y))
                    cal.show_f1()
                    break
    elif int(choice) == 2:
        print("===========================================================================================")
        print("1 - получить день\n2 - получить месяц\n3 - получить год")
        print("===========================================================================================")
        choice3 = input("Выберете одну из предложенных операций: ")
        while not choice3.isdigit() or int(choice3) < 1 or int(choice3) > 3:
            choice3 = input("Выберете одну из предложенных операций: ")
        print("===========================================================================================")
        if int(choice3) == 1:
            cal.show_day()
        elif int(choice3) == 2:
            cal.show_month()
        elif int(choice3) == 3:
            cal.show_year()
    elif int(choice) == 3:
        print("===========================================================================================")
        cal.show_f1()
    elif int(choice) == 4:
        print("===========================================================================================")
        cal.show_f2()
    elif int(choice) == 5:
        print("===========================================================================================")
        print(f"Дата до изменения: ", end="")
        cal.show_f1()
        cal.day_one()
        print(f"Дата после изменения: ", end="")
        cal.show_f1()
