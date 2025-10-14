import json
from socket import *
from algorithm import dec, brute_force, freq_analysis

server = socket()
server.bind(('localhost', 5000))
server.listen(1)

print('Server : Waiting for client....')
conn, add = server.accept()
print(f"Server : Connected {add}")
data = conn.recv(8192).decode()

try:
    shift_val, cipher = json.loads(data)
except Exception:
    shift_val = None
    cipher = data.strip()

print(f"Received cipher:\n{cipher}\nShift (parsed): {shift_val}")

if shift_val is not None:
    shift = int(shift_val)
    plain_text = dec(cipher, shift)
    print(f"Decrypted Text is {plain_text}")
    conn.send(f"Decrypted Text: {plain_text}".encode())
else:
    print("No shift provided, cannot directly decrypt with a shift.")
    guessed_shift = freq_analysis(cipher)
    guessed_message = dec(cipher, guessed_shift)
    print(f"Guessed message is {guessed_message}")
    conn.send(f"Guessed Decrypted Text: {guessed_message}".encode())

print(f"Brute Force Approch : ")
brute_force(cipher)

print(f"Frequency Analysis : ")
guessed_shift = freq_analysis(cipher)
guessed_message = dec(cipher, guessed_shift)
print(f"Guessed message is {guessed_message}")

conn.close()
