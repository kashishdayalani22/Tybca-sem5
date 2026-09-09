import string, random

def make_key(seed = None):
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.Random(seed).shuffle(shuffled)
    return dict(zip(letters, shuffled))

def substitute(text, key):
    out = ""
    for ch in text.upper():
        out += key.get(ch, ch)
    return out

key = make_key(seed = 42)
inv = {v: k for k, v in key.items()}

msg = "DEFEND THE EAST WALL"
enc = substitute(msg, key)
dec = substitute(enc, inv)
print("Key map   :", "".join(key[c] for c in string.ascii_uppercase))
print("Encrypted : ", enc)
print("Decrypted : ", dec)