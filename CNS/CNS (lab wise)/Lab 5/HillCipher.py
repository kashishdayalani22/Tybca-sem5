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

key = np.array([[3, 3], [2, 5]])
print("Encrypted :", hill_encrypt("HELP", key))