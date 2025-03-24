import socket

host = '127.0.0.1'
port = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print(f'Incomming connection from {addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            conn.sendall(data)