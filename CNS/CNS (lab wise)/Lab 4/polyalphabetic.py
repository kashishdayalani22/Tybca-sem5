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
msg = "The quick brown fox"
key = "LEMON"
enc = vigenere(msg, key)
print("Encrypted :", enc)
print("Decrypted :", vigenere(enc, key, True))