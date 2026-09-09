def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + k) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch)  - 97+ k) %26 + 97)
        elif ch.isnum():
            result += (ch + k) % 10
        else :
            result += ch    
    return result
def caecsr_decrypt(text, k):
    return caesar_encrypt(text, -k)

msg = "meet me after the toga party457"
for i in range(1, 26):
    key = i
    enc = caesar_encrypt(msg, key)
    print("with key = ", i)
    print(enc)