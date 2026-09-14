import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generate 1 MB test payload
data_1mb = get_random_bytes(1024 * 1024)

# ----------------- 1. AES-128 Timing -----------------
aes_key = get_random_bytes(16)
iv = get_random_bytes(16)

start_aes = time.perf_counter()
aes_cipher = AES.new(aes_key, AES.MODE_CBC, iv)
aes_ct = aes_cipher.encrypt(pad(data_1mb, AES.block_size))

aes_decipher = AES.new(aes_key, AES.MODE_CBC, iv)
aes_pt = unpad(aes_decipher.decrypt(aes_ct), AES.block_size)
end_aes = time.perf_counter()

aes_time = end_aes - start_aes


# ----------------- 2. RSA-2048 Timing -----------------
rsa_key = RSA.generate(2048)
rsa_pub = rsa_key.publickey()
cipher_rsa = PKCS1_OAEP.new(rsa_pub)
decipher_rsa = PKCS1_OAEP.new(rsa_key)

# RSA-2048 with OAEP can encrypt max 190 bytes per block
chunk_size = 190 
rsa_chunks = [data_1mb[i:i + chunk_size] for i in range(0, len(data_1mb), chunk_size)]

start_rsa = time.perf_counter()

# Encrypt block by block
rsa_ct_blocks = [cipher_rsa.encrypt(chunk) for chunk in rsa_chunks]

# Decrypt block by block
rsa_pt_blocks = [decipher_rsa.decrypt(chunk) for chunk in rsa_ct_blocks]
rsa_pt = b"".join(rsa_pt_blocks)

end_rsa = time.perf_counter()

rsa_time = end_rsa - start_rsa

# ----------------- Results -----------------
print(f"AES-128 Execution Time : {aes_time:.6f} seconds")
print(f"RSA-2048 Execution Time: {rsa_time:.6f} seconds")
print(f"AES is approx {rsa_time / aes_time:.2f}x faster than RSA for 1 MB data.")