# Public parameters
p, g = 23, 5

# Alice & Bob private keys
a = 6   # Alice secret
b = 15  # Bob secret

# Mallory (MitM) private keys
m_a = 9 # Key used with Alice
m_b = 4 # Key used with Bob

# 1. Alice sends A, intercepted by Mallory
A = pow(g, a, p)
M_to_alice = pow(g, m_a, p) # Mallory sends M_to_alice to Alice pretending to be Bob

# 2. Bob sends B, intercepted by Mallory
B = pow(g, b, p)
M_to_bob = pow(g, m_b, p)   # Mallory sends M_to_bob to Bob pretending to be Alice

# 3. Key computation
key_alice = pow(M_to_alice, a, p)  # Alice computes shared key with "Bob"
key_mallory_alice = pow(A, m_a, p)  # Mallory computes key shared with Alice

key_bob = pow(M_to_bob, b, p)      # Bob computes shared key with "Alice"
key_mallory_bob = pow(B, m_b, p)    # Mallory computes key shared with Bob

print("=== Man-in-the-Middle Simulation ===")
print("Alice Shared Key   :", key_alice)
print("Mallory-Alice Key  :", key_mallory_alice)
print("Bob Shared Key     :", key_bob)
print("Mallory-Bob Key    :", key_mallory_bob)

assert key_alice == key_mallory_alice
assert key_bob == key_mallory_bob
print("\nMitM Successful: Mallory intercepts all communication transparently!")