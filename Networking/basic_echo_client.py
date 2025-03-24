import socket

host = '127.0.0.1'
port = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    while True:
        text = input('Text to send: ')
        if text == 'exit':
            break
        s.send(text.encode())
        data = s.recv(1024)
        if not data:
            break
        print(data)
