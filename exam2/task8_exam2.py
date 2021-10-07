# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу
class_bal = 0
num_of_students = 0
with open("exam_task.txt") as file1:
    for line in file1.readlines():
        list_line = line.split()
        class_bal += int(list_line[2])
        num_of_students += 1
        if int(list_line[2]) <= 3:
            print(f"Ученик(ца) {list_line[0]} {list_line[1]} имеет бал {list_line[2]}")
print(f"Средний бал в классе примерно равен {class_bal // num_of_students}")


