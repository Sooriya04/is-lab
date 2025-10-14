from socket import *
from algorithm import enc
import json
client = socket()
client.connect(('localhost', 5000))

plain_text = input("Enter the message : ")
shift = int(input("Enter the shift (0-25) : "))

cipher_text = enc(plain_text, shift)

payload = [shift, cipher_text]
payload_json = json.dumps(payload).encode()
client.send(payload_json)

print(f"Client : Sent the encrypted message...")

client.close()