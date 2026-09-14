from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate 2048-bit RSA Key Pair
key = RSA.generate(2048)
pub_key = key.publickey()

msg = b"Authenticated RSA Message"
h = SHA256.new(msg)

# Sign message hash using private key
signature = pkcs1_15.new(key).sign(h)
print("Signature (hex):", signature.hex()[:64], "...")

# Verify signature using public key
h_verify = SHA256.new(msg)
try:
    pkcs1_15.new(pub_key).verify(h_verify, signature)
    print("Verification Success: Signature is VALID")
except (ValueError, TypeError):
    print("Verification Failure: Signature is INVALID")
    