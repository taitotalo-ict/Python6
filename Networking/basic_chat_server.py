from threading import Thread, Lock
import socket

host = '127.0.0.1'
port = 4000



def broadcast(message, client_socket):
    host, port = client_socket.getpeername()
    sender = f'{host}:{port}> '
    message = sender.encode() + message
    with clients_lock:
        for client in clients:
            if client == client_socket:
                continue
            client.send(message)

def client_handler(client_socket):
    while True:
        data = client_socket.recv(2048)
        if not data:
            break
        broadcast(data, client_socket)
    client_socket.close()
    with clients_lock:
        clients.remove(client_socket)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(20)

clients = []
clients_lock = Lock()

while True:
    client_socket, addr = server.accept()
    with clients_lock:
        clients.append(client_socket)
    
    Thread(target=client_handler, args=(client_socket,)).start()
