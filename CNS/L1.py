def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + k) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch)  - 97+ k) %26 + 97)
        else :
            result += ch    
    return result
def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)

msg = "meet me after the toga party"
key = 3
enc = caesar_encrypt(msg, key)
print("Plaintext :", msg)
print("Encrypted :", enc)
print("Decrypted :", caesar_decrypt(enc, key))