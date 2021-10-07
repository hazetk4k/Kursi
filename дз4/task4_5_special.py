F1 = 1
F2 = 1
n = int(input())
print(F1, F2, end=" ")
for i in range(2, n):
    F1, F2 = F2, F1 + F2
    print(F2, end=" ")
   # n -= 1
