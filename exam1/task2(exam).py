str1 = input("Введите текст из букаф: ") #а, у, о, ы, и, э, я, ю, ё, е
glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
sign = ['/','*','-','+',',','.',' ']
glas_count = 0
new_glas =''
sogl_count = 0
for i in str1:
    if i in glas:
        glas_count += 1
        new_glas += i
    elif i.isdigit() or i in sign:
        continue
    else:
        sogl_count += 1
if glas_count == sogl_count:
    print(new_glas)




