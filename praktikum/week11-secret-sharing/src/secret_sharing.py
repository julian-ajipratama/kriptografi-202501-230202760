import random

# Bilangan prima besar (harus > secret)
P = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def generate_shares(secret, k, n):
    """
    Membagi secret menjadi n shares dengan threshold k
    """
    # Koefisien polinomial acak (a0 = secret)
    coeffs = [secret] + [random.randrange(1, P) for _ in range(k - 1)]

    shares = []
    for x in range(1, n + 1):
        y = 0
        for i in range(len(coeffs)):
            y += coeffs[i] * (x ** i)
        y %= P
        shares.append((x, y))
    return shares

def reconstruct_secret(shares):
    """
    Rekonstruksi secret menggunakan Lagrange Interpolation
    """
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        lj = 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                lj *= xm * pow(xm - xj, -1, P)
                lj %= P
        secret += yj * lj
        secret %= P
    return secret

# ===== MAIN PROGRAM =====
secret = 123456  # rahasia (integer)
k = 3
n = 5

shares = generate_shares(secret, k, n)

print("Shares yang dihasilkan:")
for s in shares:
    print(s)

# Rekonstruksi dengan k shares
recovered = reconstruct_secret(shares[:k])
print("\nRecovered secret:", recovered)