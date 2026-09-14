import hashlib

def get_hashes(msg):
    data = msg.encode()
    return hashlib.sha1(data).hexdigest(), hashlib.sha256(data).hexdigest()

def hex_to_bin(hex_str):
    num_bits = len(hex_str) * 4
    return bin(int(hex_str, 16))[2:].zfill(num_bits)

def count_bit_diff(hash1_hex, hash2_hex):
    bin1 = hex_to_bin(hash1_hex)
    bin2 = hex_to_bin(hash2_hex)
    return sum(b1 != b2 for b1, b2 in zip(bin1, bin2)), len(bin1)

msg1 = "Hello World"
msg2 = "Hello world"  # 1-character case change

sha1_1, sha256_1 = get_hashes(msg1)
sha1_2, sha256_2 = get_hashes(msg2)

# Bit differences
sha1_diff, sha1_total = count_bit_diff(sha1_1, sha1_2)
sha256_diff, sha256_total = count_bit_diff(sha256_1, sha256_2)

print("=== Avalanche Effect Quantified ===")
print(f"Message 1: '{msg1}'")
print(f"Message 2: '{msg2}'\n")

print(f"SHA-1 Digest 1 : {sha1_1}")
print(f"SHA-1 Digest 2 : {sha1_2}")
print(f"SHA-1 Bit Flips: {sha1_diff}/{sha1_total} bits ({(sha1_diff/sha1_total)*100:.2f}%)\n")

print(f"SHA-256 Digest 1 : {sha256_1}")
print(f"SHA-256 Digest 2 : {sha256_2}")
print(f"SHA-256 Bit Flips: {sha256_diff}/{sha256_total} bits ({(sha256_diff/sha256_total)*100:.2f}%)")