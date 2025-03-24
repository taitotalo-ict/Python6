import socket

host = '127.0.0.1'
port = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.send(b'Moi')
    data = s.recv(1024)
    print(data)
