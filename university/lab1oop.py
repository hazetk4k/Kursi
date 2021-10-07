a = input()
count = 1
str1 = ""
for i in a:
    if count == 1:
        str1 += hex(ord(i))
        count += 1
    else:
        str1 += hex(ord(i))
print(str1.center(50).replace(" ", "$"))
