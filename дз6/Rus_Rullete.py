from random import randint

player_list = []
dead = []
count = 1
bullet_place = 0

print("\t$Русская рулетка$")
player_kol = int(input("Введите количество желающих поучавствовать...: "))

for i in range(player_kol):
    name = input(f"\tВведите имя участника {count}: ")
    while name in player_list:
        name = input(f"\tИмя должно быть оригинальным, номер {count}: ")
    player_list.append(name)
    count += 1

while player_kol != 1:
    list_count = 0
    for i in range(len(player_list)):
        if player_list[list_count] in dead:
            list_count += 1
            continue
        bullet_place = (randint(1, 6))
        #эту строчку добавил для проверки, чтобы стразу угадывать и умирать
        print(bullet_place)
        print("=======================================================================================================")
        choice = int(input(f"{player_list[list_count]}, как думаешь, на какой позиции пуля?: "))
        while choice < 0 and choice > 6:
            choice = int(input(f"{player_list[list_count]}, ты чего? Всего 6 мест. Выбирай: "))
        if choice == bullet_place:
            print(f"\n!!!Бах!!!\nК сожалению ты угадал... Игрок {player_list[list_count]} выбыл...")
            dead.append((player_list[list_count]))
            list_count += 1
            player_kol -= 1
        else:
            print(f"\nТы не угадал. Ну и хорошо. Следующий!")
            list_count += 1
        print("=======================================================================================================")
# следующая строка нужна для того, чтобы выйти из цикла вайл во время первой итерации, если все игроки - неудачники
        if len(dead) == len(player_list) - 1:
            break
print("\tТоп игроков:")
for _ in player_list:
    if _ in dead:
        continue
    else:
        print(f"1: {_} (выжил)")
counter = 2
for i in dead[::-1]:
    print(f"{counter}: {i}")
    counter += 1

