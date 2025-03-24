import socket

# host = 'taitotalo.fi'
host = 'httpbin.org'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

http_request = f'''GET / HTTP/1.1\r\nHost: {host}\r\n\r\n'''
s.send(http_request.encode())

while True:
    data = s.recv(16*1024)
    if not data:
        break
    http_response = data.decode()
    print(http_response)

s.close()