n = int(input())
num = 1
for i in range(n):
    for _ in range(i+1):
        h = str(num * (i+1))
        print(h, end="")



