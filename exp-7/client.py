from socket import *
from random import *

client = socket()
client.connect(('localhost', 3000))
print('[Client] is connected.....')

data = client.recv(1024).decode()
g, p, A = map(int, data.split(','))
b = randint(1, p - 2)

B = pow(g, b, p)

client.send(f"{B}".encode())

shared_key = pow(A, b, p)
print(f'Shared key is {shared_key}')

client.close()