from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Two identical 16-byte blocks
msg_repeating = b"ABCDEFGHIJKLMNOPABCDEFGHIJKLMNOP" 

key = get_random_bytes(16)  # 128-bit key
cipher = AES.new(key, AES.MODE_ECB)
ct = cipher.encrypt(pad(msg_repeating, AES.block_size))

# Extracting first two 16-byte ciphertext blocks
block1 = ct[:16].hex()
block2 = ct[16:32].hex()

print("Block 1 (hex):", block1)
print("Block 2 (hex):", block2)
print("Identical ciphertext blocks?:", block1 == block2)