str1 = input()
count_niz = 0
count_vverh = 0
sum = ''
for i in range(len(str1) -1):
    sum = str1[i] + str1[i+1]
    if not sum.isalpha:
        continue
    if sum.islower():
        count_niz += 1
    elif sum.isupper():
        count_vverh += 1
print(f"Нижнего регистра {count_niz} и верхнего регистра{count_vverh}")

