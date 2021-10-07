sep = "=" * 50


class Game:
    def __init__(self):
        self.matrix = [["/", "/", "/"], ["/", "/", "/"], ["/", "/", "/"]]

    def table(self):
        print(f"   │ x │ x │ x │")
        print("───┼───┼───┼───┼")
        print(f" y │ {self.matrix[0][0]} │ {self.matrix[0][1]} │ {self.matrix[0][2]} │")
        print("───┼───┼───┼───┼")
        print(f" y │ {self.matrix[1][0]} │ {self.matrix[1][1]} │ {self.matrix[1][2]} │")
        print("───┼───┼───┼───┼")
        print(f" y │ {self.matrix[2][0]} │ {self.matrix[2][1]} │ {self.matrix[2][2]} │")

    def Win_Check(self, Xo, player):
        for i in range(3):
            if self.matrix[i][0] + self.matrix[i][1] + self.matrix[i][2] in (Xo + Xo + Xo):
                print(
                    f"{sep}\n{player} Побеждает!\n{sep}")
                return True
        for j in range(3):
            if self.matrix[0][j] + self.matrix[1][j] + self.matrix[2][j] in (Xo + Xo + Xo):
                print(
                    f"{sep}\n{player} Побеждает!\n{sep}")
                return True
        if self.matrix[0][0] + self.matrix[1][1] + self.matrix[2][2] in (Xo + Xo + Xo):
            print(
                f"{sep}\n{player} Побеждает!\n{sep}")
            return True
        if self.matrix[0][2] + self.matrix[1][1] + self.matrix[2][0] in (Xo + Xo + Xo):
            print(
                f"{sep}\n{player} Побеждает!\n{sep}")
            return True

    def change_table(self, i, j, player):
        if player == name1:
            self.matrix[int(i) - 1][int(j) - 1] = "X"
        else:
            self.matrix[int(i) - 1][int(j) - 1] = "O"

    def check_taken(self, i, j):
        if self.matrix[int(i) - 1][int(j) - 1] != "/":
            print("Эта клетка занята! Выбери другую!")
            return "Error"


print("\tКрестики - нолики")
name1 = input("Введите имя игрока 1(крестики): ")
name2 = input("Введите имя игрока 2(нолики): ")
while True:
    game = Game()
    print("\tНачнем игру!")
    count = 1
    game.table()
    while True:
        print(sep)
        if count % 2 == 0:
            print(f"Ход игрока {name2}")
        else:
            print(f"Ход игрока {name1}")
        num1 = input("Введите x: ")
        while not num1.isdigit() or int(num1) < 0 or int(num1) > 3:
            num1 = input("Введите x(число от 1 до 3): ")
        num2 = input("Введите y: ")
        while not num2.isdigit() or int(num2) < 0 or int(num2) > 3:
            num1 = input("Введите y(число от 1 до 3): ")
        if game.check_taken(num2, num1) == "Error":
            continue
        else:
            if not count % 2 == 0:
                game.change_table(num2, num1, name1)
                game.table()
                if game.Win_Check("X", name1) == True:
                    break
            else:
                game.change_table(num2, num1, name2)
                game.table()
                if game.Win_Check("O", name1) == True:
                    break
        count += 1
        if count > 9:
            print(f"{sep}\nНичья!\n{sep}")
            break
    quest = input("\n1 - Повторить игру\n2 - Выход\nХотите повторить игру?: ")
    while not quest.isdigit() or int(quest) > 2 or int(quest) < 1:
        quest = input("\n1 - Повторить игру\n2 - Выход\nХотите повторить игру?(да выбери ты нормально 1 или 2!!!): ")
    if int(quest) == 1:
        continue
    else:
        print("Спасибо за игру!")
        break
