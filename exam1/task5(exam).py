str1 = input("Введите что-нибудь: ")
list1 = str1.split(' ')
for i in list1:
    if i.isdigit():
        print(i)
