from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
key = RSA.generate(2048)
pub = key.publickey()
msg = b"Secret message for RSA"
enc_cipher = PKCS1_OAEP.new(pub)
ct = enc_cipher.encrypt(msg)
print("Encrypted (hex):", ct.hex()[:64], "...")
dec_cipher = PKCS1_OAEP.new(key)
pt = dec_cipher.decrypt(ct)
print("Decrypted      :", pt.decode())