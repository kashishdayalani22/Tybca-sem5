p = 23      # public prime (small, for demo)
g = 5       # public generator
a = 6       # Alice's secret
b = 15      # Bob's secret
A = pow(g, a, p)     # Alice sends A
B = pow(g, b, p)     # Bob sends B
alice_secret = pow(B, a, p)
bob_secret   = pow(A, b, p)
print(f"Alice public A = {A}, Bob public B = {B}")
print("Alice shared secret :", alice_secret)
print("Bob shared secret   :", bob_secret)
assert alice_secret == bob_secret
print("Shared key agreed!")