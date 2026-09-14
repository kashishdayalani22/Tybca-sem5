from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
key = RSA.generate(2048)
pub = key.publickey()
msg = b"Transfer 1000 to account 12345"
h = SHA256.new(msg)
signature = pkcs1_15.new(key).sign(h)
print("Signature (hex):", signature.hex()[:64], "...")
# Verification
h2 = SHA256.new(msg)
try:
    pkcs1_15.new(pub).verify(h2, signature)
    print("Signature is VALID")
except (ValueError, TypeError):
    print("Signature is INVALID")
# Tamper test
h3 = SHA256.new(b"Transfer 9999 to account 12345")
try:
    pkcs1_15.new(pub).verify(h3, signature)
    print("Tampered message accepted (should not happen)")
except (ValueError, TypeError):
    print("Tampered message correctly REJECTED")