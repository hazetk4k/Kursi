import socket

# клиентский сокет
client_socket = socket.socket()

# предложение для выполнения логики
sen = input("Input number from 0 to 10: ")
while not sen.isdigit() or int(sen) < 0 or int(sen) > 10:
    sen = input("Input number from 0 to 10: ")
# присоединяемся к серверу и отправляем сообщение
client_socket.connect(('localhost', 6161))
client_socket.send(bytes(sen, encoding='UTF-8'))

data = client_socket.recv(1024)

print(data)

# закрываем соединение
client_socket.close()
