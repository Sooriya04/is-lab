p = 47
g = 2

from socket import *
from random import *

server = socket()
print('[Server] is waiting....')
server.bind(('localhost', 3000))
server.listen(1)
conn, addr = server.accept()
print('[Server] is connected.....')

a = randint(1, p - 2)

A = pow(g, a, p)
conn.send(f"{g},{p},{A}".encode())

data = conn.recv(1024).decode()

B = int(data)

shared_key = pow(B, a, p)
print(f'Shared key is {shared_key}')

conn.close()