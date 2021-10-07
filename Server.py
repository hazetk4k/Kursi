import socket

# серверный сокет
server_socket = socket.socket(socket.AF_INET,  # задаём семейтво протоколов(INET)
                              socket.SOCK_STREAM,  # задаем протокол передачт(TCP)
                              proto=0)  # выбираем протокол для TCP (IP)

server_socket.bind(('', 6161))
server_socket.listen(1)

connection, address = server_socket.accept()

print("Connected:", address)

# настройка и логика сервера

while True:

    data = connection.recv(1024).decode()
    if not data:
        break
    rezult = ""
    if data == "1":
        rezult = "one"
    elif data == "2":
        rezult = "two"
    elif data == "3":
        rezult = "three"
    elif data == "4":
        rezult = "four"
    elif data == "5":
        rezult = "five"
    elif data == "6":
        rezult = "six"
    elif data == "7":
        rezult = "seven"
    elif data == "8":
        rezult = "eight"
    elif data == "9":
        rezult = "nine"
    elif data == "10":
        rezult = "ten"
    elif data == "0":
        rezult = "zero"
    connection.send(bytes(rezult, encoding='UTF-8'))

# закрываем соединения

connection.close()
