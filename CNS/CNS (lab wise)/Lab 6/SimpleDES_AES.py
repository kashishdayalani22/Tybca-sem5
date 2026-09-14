from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
key = get_random_bytes(16)      # AES-128
iv  = get_random_bytes(16)
msg = b"Cryptography Network Security Lab"
cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(msg, AES.block_size))
print("Ciphertext (b64):", base64.b64encode(ct).decode())
decipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(decipher.decrypt(ct), AES.block_size)
print("Decrypted       :", pt.decode())