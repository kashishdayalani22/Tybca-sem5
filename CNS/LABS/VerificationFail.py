from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Senders Key Pair
sender_key = RSA.generate(2048)

# Unrelated Third-Party Key Pair
wrong_key = RSA.generate(2048)
wrong_pub_key = wrong_key.publickey()

msg = b"Transfer 1000 to account 12345"
h = SHA256.new(msg)

# Sign message hash with sender's private key
signature = pkcs1_15.new(sender_key).sign(h)

# Attempt verification using the wrong public key
try:
    pkcs1_15.new(wrong_pub_key).verify(h, signature)
    print("Verification Success: Signature accepted.")
except (ValueError, TypeError):
    print("Verification Failed: Signature rejected (Wrong Public Key used).")