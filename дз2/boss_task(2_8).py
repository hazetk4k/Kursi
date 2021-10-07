env_x, env_y = 10, 7
#pap_x, pap_y = 8, 9
#pap_x, pap_y = 9, 8
#pap_x, pap_y = 6, 8
#pap_x, pap_y = 8, 6
#pap_x, pap_y = 3, 4
#pap_x, pap_y = 11, 9
#pap_x, pap_y = 9, 11
if env_x >= pap_x:
    if env_y >= pap_y:
        print("da")
    elif env_y < pap_y:
        if env_x >= pap_y and env_y >= pap_x:
            print("da")
        else:
            print("net")
elif env_x < pap_x:
    if env_y >= pap_x and env_x >= pap_y:
        print("da")
    else:
        print("net")
