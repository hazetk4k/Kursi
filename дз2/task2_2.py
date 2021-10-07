age = input("How old are you?\n")
if int(age) <= 0:
    print("Wrong input!")
elif int(age)>0 and int(age)<18:
    print("CocaCola")
else:
    print("Beer")


