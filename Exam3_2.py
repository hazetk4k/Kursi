def palindrom(str1):
    r = str1[::-1]
    if str1 == r:
        return "палиндром"
    else:
        return "не палиндром"


res = palindrom("доводы")
print(f'Нолон сказал, это {res}')
