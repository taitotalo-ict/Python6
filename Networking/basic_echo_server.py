import socket
from threading import Thread

host = '127.0.0.1'
port = 50000

def listener(conn, addr):
    print(f'Incomming connection from {addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        # Käynnistää uusi thread
        thread = Thread(target=listener, args=(conn, addr))
        thread.start()

        