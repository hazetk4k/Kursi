import socket

# клиентский сокет
client_socket = socket.socket()

# предложение для выполнения логики
sen = input("Input sentences: ")

# присоединяемся к серверу и отправляем сообщение
client_socket.connect(('localhost', 7777))
client_socket.send(bytes(sen, encoding='UTF-8'))

data = client_socket.recv(1024)

print(data)

# закрываем соединение
client_socket.close()
