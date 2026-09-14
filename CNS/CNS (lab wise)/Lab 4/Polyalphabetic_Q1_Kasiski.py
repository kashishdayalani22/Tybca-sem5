def vigenere(text, key, decrypt=False):
    result, ki = "", 0
    key = key.upper()
    for ch in text:
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - 65
            if decrypt:
                shift = -shift
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
            ki += 1
        else:
            result += ch
    return result


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_repeat_spacings(ciphertext, seq_len=3):
    ciphertext = "".join([ch for ch in ciphertext.upper() if 'A' <= ch <= 'Z'])
    spacings = []
    
    for i in range(len(ciphertext) - seq_len):
        seq = ciphertext[i:i + seq_len]
        for j in range(i + seq_len, len(ciphertext) - seq_len + 1):
            if ciphertext[j:j + seq_len] == seq:
                spacings.append(j - i)
                
    return spacings

def kasiski_test(ciphertext):
    spacings = find_repeat_spacings(ciphertext, seq_len=3)
    
    if not spacings:
        print("No repeated sequences found.")
        return
        
    print("Spacings found between repeated trigrams:", spacings)
    
    overall_gcd = spacings[0]
    for dist in spacings[1:]:
        overall_gcd = gcd(overall_gcd, dist)
        
    print(f"Estimated Key Length (GCD of spacings): {overall_gcd}")


msg = "The quick brown fox"
key = "LEMON"
enc = vigenere(msg, key)
print("Encrypted :", enc)
print("Decrypted :", vigenere(enc, key, True))

kasiski_test(enc)