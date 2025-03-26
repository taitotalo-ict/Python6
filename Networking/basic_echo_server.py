import socket
from threading import Thread

host = '127.0.0.1'
port = 50000
shutdown = False

def communicator(conn, addr):
    global shutdown
    print(f'Incomming connection from {addr}')
    with conn:
        while not shutdown:
            try:
                data = conn.recv(1024)
            except TimeoutError:
                continue
            if not data:    # data = b''
                # Asiakas on sulkenut yhteyden
                break
            # if data == b'shutdown':
            #     shutdown = True
            #     break
            print(data)
            conn.sendall(data)

def listener():
    socket.setdefaulttimeout(0.3)   # 0.3s = 300ms
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        while not shutdown:
            try:
                conn, addr = s.accept()
            except TimeoutError:
                continue
            # Käynnistää uusi thread
            thread = Thread(target=communicator, args=(conn, addr))
            thread.start()

Thread(target=listener).start()
while True:
    text = input('')
    if text == 'exit':
        shutdown = True
        break

