# 2.1.Необходимо реализовать модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
# 2.2.Создать двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.


class Human:

    def __init__(self, hunger, day, food, money, joy):
        self.hunger = hunger
        self.day = day
        self.food = food
        self.money = money
        self.joy = joy

    def eat(self):
        if self.food <= 0:
            print("Хм... Холодильник пуст")
            print("================================================================")
            return None
        print('"Скушал пиццы"\n+50 сытости')
        print("================================================================")
        self.hunger += 50
        self.food -= 1
        self.joy += 5

    def work(self):
        print('"Опять работать?"\n- 20 сытости')
        print("================================================================")
        self.hunger -= 20
        self.money += 100
        self.joy -= 20

    def play(self):
        print('"Поиграю немного, а потом ещё чуть-чуть))))"\n-10 сытости')
        print("================================================================")
        self.hunger -= 10
        self.joy += 50

    def go_to_shop(self):
        if self.money < 20:
            print("Денег не хватает")
            print("================================================================")
            return None
        print('"Пора купить пиццы"\n +5 ед. еды')
        print("================================================================")
        self.hunger -= 5
        self.money -= 20
        self.joy -= 10
        return None

    def death(self):
        if self.hunger <= 0:
            print('Вы погибли от голода\nЗаключение врача: "Острый недостаток пиццы в организме на последней стадии"')
            print("================================================================")
            return "death"
        elif self.joy <= 0:
            print('Вы погибли от грусти\nЗаключение врача: "Истощение организма вследсвие депрессии"')
            print("================================================================")
            return "death"
        else:
            self.day += 1
            return "next_day"

    def stats(self):
        print(f"День: {self.day}\nГолод: {self.hunger}\nРадость: {self.joy}\nДеньги: {self.money}\nПицца: {self.food}")
        print("================================================================")

    def final(self):
        print(f"Дней прожито: {self.day}\nДеньги: {self.money}\nЕда в холодильнике: {self.food}")


human = Human(50, 0, 7, 50, 50)
print("Вы - человек. Вы можете заниматься чем угодно из данных вам вариантов.")
print("Но помните: если кол-во очков голода или радости будет равно 0, вы умрете.\nВаша задача - прожить 365 дней")
print("================================================================")
while 1:
    print("1 - Работать\n2 - Играть\n3 - Есть\n4 - Сходить в магазин")
    print("================================================================")
    choice = int(input("Введите номер выбранного действия: "))
    if choice == 1:
        human.work()
    elif choice == 2:
        human.play()
    elif choice == 3:
        human.eat()
    elif choice == 4:
        human.go_to_shop()
    elif choice == 5:
        print('Вы решили уйти')
        break
    print("\n\n\n")
    human.stats()
    if human.death() == "death":
        break
human.final()
