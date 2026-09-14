from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key_256 = get_random_bytes(32)  # 256-bit key (32 bytes)
iv = get_random_bytes(16)
msg = b"Cryptography Network Security Lab"

# Encryption
cipher = AES.new(key_256, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(msg, AES.block_size))
print("Encrypted (hex):", ct.hex())

# Decryption
decipher = AES.new(key_256, AES.MODE_CBC, iv)
pt = unpad(decipher.decrypt(ct), AES.block_size)
print("Decrypted      :", pt.decode())