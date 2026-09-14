def build_matrix(key):
    key = key.upper().replace("J", "I")
    seen, matrix = [], []
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    return [seen[i:i+5] for i in range(0, 25, 5)]

def find(matrix, ch):
    for r, row in enumerate(matrix):
        if ch in row:
            return r, row.index(ch)
        
def prepare(text):
    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c.isalpha())
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            pairs.append(a + "X"); i += 1
        else:
            pairs.append(a + b); i += 2
    if len(pairs[-1]) == 1:
        pairs[-1] += "X"
    return pairs

def playfair_encrypt(text, key):
    m = build_matrix(key)
    out = ""
    for pair in prepare(text):
        r1, c1 = find(m, pair[0])
        r2, c2 = find(m, pair[1])
        if r1 == r2:
            out += m[r1][(c1+1) % 5] + m[r2][(c2+1) % 5]
        elif c1 == c2:
            out += m[(r1+1) % 5][c1] + m[(r2+1) % 5][c2]
        else:
            out += m[r1][c2] + m[r2][c1]
    return out

def playfair_decrypt(text, key):
    m = build_matrix(key)
    out = ""
    for pair in prepare(text):
        r1, c1 = find(m, pair[0])
        r2, c2 = find(m, pair[1])
        if r1 == r2:
            out += m[r1][(c1-1) % 5] + m[r2][(c2-1) % 5]
        elif c1 == c2:
            out += m[(r1-1) % 5][c1] + m[(r2-1) % 5][c2]
        else:
            out += m[r1][c2] + m[r2][c1]
    if out[-1] == 'X':
        out = out[:-1]
    return out


k = "MONARCHY"
msg = "Hide the gold"

enc = playfair_encrypt(msg, k)
print(enc)

print()
dec = playfair_decrypt(enc, k)
print(dec)