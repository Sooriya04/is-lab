def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def inv_mod(a, p):
    g, x, _ = egcd(a, p)
    if g != 1:
        raise Exception("No modular inverse exists")
    return x % p

def point_add(P, Q, a, p):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = ((3 * x1 * x1 + a) * inv_mod(2 * y1, p)) % p
    else:
        m = ((y2 - y1) * inv_mod(x2 - x1, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(k, P, a, p):
    result = None 
    addend = P

    while k:
        if k & 1:
            result = point_add(result, addend, a, p)
        addend = point_add(addend, addend, a, p)
        k >>= 1
    return result

def find_generator(a, b, p):
    
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if (y*y) % p == rhs:
                return (x, y)
    return None

if __name__ == "__main__":
    print("=== Simple ECC Key Generator ===")

    p = int(input("Enter a prime modulus p: "))
    a = int(input("Enter curve coefficient a: "))
    b = int(input("Enter curve coefficient b: "))

    G = find_generator(a, b, p)
    if G is None:
        print("generator not found!")
        exit()

    print(f"Generator point G found: {G}")

    priv = int(input("Enter your private key (integer): "))
    pub = scalar_mult(priv, G, a, p)

    print("ECC Parameters")
    print(f"Curve: y² = x³ + {a}x + {b} (mod {p})")
    print(f"Generator (G): {G}")
    print(f"Private key : {priv}")
    print(f"Public key  : {pub}")
