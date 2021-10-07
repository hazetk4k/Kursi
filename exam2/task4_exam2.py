# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.
str1 = 'An apple a day keeps the doctor away'
list_used = []
dict1 = {}
for i in str1:
    if i in list_used:
        continue
    else:
        list_used.append(i)
        dict1[i] = str1.count(i)
print(dict1)
