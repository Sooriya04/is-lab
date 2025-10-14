import math
p = int(input("Enter first prime number (e.g., 61): "))
q = int(input("Enter second prime number (e.g., 53): "))
e = int(input("Enter public key (e.g., 17): "))
message = input("Enter text: ")

n = p * q
phi = (p - 1) * (q - 1)

if math.gcd(phi, e) != 1:
    print('not coprime')
    exit()

d = pow(e, -1, phi)

message_num = [ord(c) for c in message]

encrypt_nums = [pow(m, e, n) for m in message_num]
print(encrypt_nums)

decrypt_nums = [pow(c, d, n) for c in encrypt_nums]
print(decrypt_nums)

org_msg = ''

for num in decrypt_nums:
    org_msg += chr(num)

print(org_msg)