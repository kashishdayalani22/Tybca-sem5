import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    nums = [ord(c) - 65 for c in text]
    out = ""
    for i in range(0, len(nums), 2):
        vec = np.array([nums[i], nums[i+1]])
        res = key.dot(vec) % 26
        out += chr(int(res[0]) + 65) + chr(int(res[1]) + 65)
    return out

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def mod_inverse(a, m=26):
    a = a % m
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"Determinant {a} shares a factor with {m} (gcd = {g}). Key is NOT invertible mod {m}.")
    return x % m

def matrix_mod_inv(key, m=26):
    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % m
    inv_det = mod_inverse(det, m)
    
    adj = [
        [key[1][1] % m, (-key[0][1]) % m],
        [(-key[1][0]) % m, key[0][0] % m]
    ]
    
    inv_key = [
        [(inv_det * adj[0][0]) % m, (inv_det * adj[0][1]) % m],
        [(inv_det * adj[1][0]) % m, (inv_det * adj[1][1]) % m]
    ]
    return inv_key

def hill_decrypt(ciphertext, key):
    inv_key = matrix_mod_inv(key)
    nums = [ord(c) - 65 for c in ciphertext.upper()]
    out = ""
    for i in range(0, len(nums), 2):
        c1, c2 = nums[i], nums[i+1]
        p1 = (inv_key[0][0] * c1 + inv_key[0][1] * c2) % 26
        p2 = (inv_key[1][0] * c1 + inv_key[1][1] * c2) % 26
        out += chr(p1 + 65) + chr(p2 + 65)
    return out


invalid_key = np.array([[2, 4], [1, 5]])
print("\nTesting Invalid Key Matrix:")
try:
    hill_decrypt("HELP", invalid_key)
except ValueError as e:
    print("Caught Error:", e)