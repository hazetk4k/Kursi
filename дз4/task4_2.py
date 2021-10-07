m = int(input("m = "))
n = int(input("n = "))
if m < n:
    r = n - m
    for i in range(r + 1):
        print(m)
        m += 1
else:
    r = m - n
    for i in range(r + 1):
        print(m)
        m -= 1
