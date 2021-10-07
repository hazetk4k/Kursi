count = 1
step1 = 1
step2 = 4
while count != 6:
    place = 1
    for i in range(step1, step2 + 1):
        print(f"{i} в ширенге занимает шеренгу {place}")
        place += 1
    step1 += 4
    step2 += 4
    count += 1

