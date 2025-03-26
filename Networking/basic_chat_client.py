from threading import Thread
import socket

host = '172.20.21.200'
port = 4000


def receiver(client: socket) -> None:
    while not shutdown:
        data = client.recv(2048)
        if not data:
            break
        print('Received: ', data.decode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
shutdown = False

Thread(target=receiver, args=(client, )).start()

while True:
    message = input('Enter message: ')
    if message == 'exit':
        shutdown = True
        break
    client.send(message.encode())



