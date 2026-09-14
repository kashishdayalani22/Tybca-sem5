import string, random

def make_key(seed=None):
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.Random(seed).shuffle(shuffled)
    return dict(zip(letters, shuffled))

def substitute(text, key):
    out = ""
    for ch in text.upper():
        out += key.get(ch, ch)
    return out

def analyze_frequency(ciphertext):

    ENGLISH_FREQ = {
    'E': 12.70, 'T': 9.06,  'A': 8.17,  'O': 7.51,  'I': 6.97,  'N': 6.75, 'S': 6.33,  'H': 6.09,  'R': 5.99,  'D': 4.25,  'L': 4.03,  'C': 2.78, 'U': 2.76,  'M': 2.41,  'W': 2.36,  'F': 2.23,  'G': 2.02,  'Y': 1.97, 'P': 1.93,  'B': 1.49,  'V': 0.98,  'K': 0.77,  'J': 0.15,  'X': 0.15, 'Q': 0.10,  'Z': 0.07
}

    counts = {}
    total_letters = 0

    for ch in ciphertext.upper():
        if 'A' <= ch <= 'Z':
            counts[ch] = counts.get(ch, 0) + 1
            total_letters += 1
            
    if total_letters == 0:
        return

    alphabet = [chr(i) for i in range(65, 91)]
    sorted_letters = sorted(alphabet, key=lambda x: counts.get(x, 0), reverse=True)

    print("Letter | Count | Observed (%) | Expected (%)")
    print("-" * 44)
    for char in sorted_letters:
        count = counts.get(char, 0)
        obs_freq = (count / total_letters) * 100
        exp_freq = ENGLISH_FREQ[char]
        print(f"{char:<6} | {count:<5} | {obs_freq:<12.2f} | {exp_freq:<12.2f}")

key = make_key(seed=42) 
inv = {v: k for k, v in key.items()} 
msg = "DEFEND THE EAST WALL"
enc = substitute(msg, key)
dec = substitute(enc, inv)
print("Key map   :", "".join(key[c] for c in string.ascii_uppercase))
print("Encrypted :", enc)
print("Decrypted :", dec)
print()
analyze_frequency(enc )