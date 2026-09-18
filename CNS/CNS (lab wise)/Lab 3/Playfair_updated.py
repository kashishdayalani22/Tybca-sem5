import numpy as np

def build_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in matrix:
            matrix.append(ch)
    matrix = np.reshape(matrix, (5, 5))
    return matrix

def find(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def prepare(text):
    s = ""
    for ch in text:
        if ch.isalpha():
            s += ch.upper()
    
    pairs = []
    i = 0
    while i < len(s):
        a = s[i]
        if i + 1 < len(s):
            b = s[i + 1]
        else:
            b = "X"

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    return pairs

def Playfair_enc(text, key):
    matrix = build_matrix(key)
    res = ""
    for pair in prepare(text):
        r1, c1 = find(matrix, pair[0])
        r2, c2 = find(matrix, pair[1])

        if r1 == r2:
            res += matrix[r1][(c1+1) % 5] + matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            res += matrix[(r1+1) % 5][c1] + matrix[(r2+1) % 5][c2]
        else:
            res += matrix[r1][c2] + matrix[r2][c1]
    return res

print(Playfair_enc("Hide the gold", "MONARCHY"))