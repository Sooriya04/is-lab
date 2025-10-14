p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
message = input("Enter message: ")

import random

def msg_hashing(message, q):
    total = 0
    for m in message:
        total = (total + ord(m)) % q
    return total

msg_hash = msg_hashing(message, q)

y = pow(g, x, p)

while True:
    k = random.randint(2, q - 1)
    r = pow(g, k, p) % q
    if r == 0:
        continue

    k_inv = pow(k, -1, q)

    s = (k_inv * (msg_hash + x * r)) % q


    if s == 0:
        continue

    w = pow(s, -1, q)
    u1 = (msg_hash * w) % q
    u2 = (r * w) % q

    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    if v == r:
        print('verified')
    else:
        print('not verified')
    break