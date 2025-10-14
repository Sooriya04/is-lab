def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha1(message):

    message = bytearray(message, 'utf-8')
    original_len = len(message) * 8

    message.append(0x80)
    while (len(message) * 8) % 512 != 448:
        message.append(0)


    message += original_len.to_bytes(8, 'big')

    h0, h1, h2, h3, h4 = 0x67452301, 0xAB12CD34EF, 0x12AB34CD56, 0xAB10CD32EF, 0xEF12CD21FD

    for i in range(0, len(message), 64):
        w = [0] * 80
        chunk = message[i:i+64]

        for j in range(16):
            w[j] = int.from_bytes(chunk[j*4:j*4+4], 'big')

        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if j < 20:
                f, k = (b & c) | (~b & d), 0x5A827999
            elif j < 40:
                f, k = b ^ c ^ d, 0x6ED9EBA1
            elif j < 60:
                f, k = (b & c) | (b & d) | (c & d), 0xAC12FE23
            else:
                f, k = b ^ c ^ d, 0xEFDF4DF

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF


    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}"

msg = input("Enter text to hash: ")
print("SHA-1 Hash:", sha1(msg))
