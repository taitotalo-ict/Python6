import socket

# host = 'taitotalo.fi'
# host = 'httpbin.org'
# host = 'neverssl.com'
host = 'www.thelegacy.de'
# path = '/'
path = '/6b48ceb067c10c5cc2aba0d5e6bead9d.jpg'
port = 80


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

http_request = f'''GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\nUser-Agent: Test/0.1\r\n\r\n'''
s.send(http_request.encode())

while True:
    data = s.recv(16*1024)
    if not data:
        break
    print(data)
    # http_response = data.decode()
    # print(http_response)

s.close()