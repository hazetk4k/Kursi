# пришлось подумать, возможно можно и проще, но я только так придумал
n = int(input())
for i in range(1, n + 1):
    h = i
    print(i, end="")
    for p in range(1, i + 1):
        if h != 0:
            if i % h == 0:
                print("*", end="")
                h = h - 1
            else:
                h = h - 1
                print(end="")
        else:
            continue
    print()
