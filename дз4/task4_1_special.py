# print(int(a[0]) + int(a[1]) + int(a[2])) тоже работает вроде, после a = input() конечно
n = 0
p = 0
a = input()
for i in range(int(3)):
    n = n + int(a[p])
    p += 1
print(n)
