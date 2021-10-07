n = int(input())
for i in range(n):
    if 5 < i + 1 < 12 or 14 < i + 1 < 26 or 31 < i + 1 < 40:
        continue
    print(i + 1)
