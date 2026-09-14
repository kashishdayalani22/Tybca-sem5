import time

def brute_force_dlp(g, target, p):
    for x in range(1, p):
        if pow(g, x, p) == target:
            return x
    return None

# Case 1: Small prime (Insecure)
p_small, g = 23, 5
a_secret = 6
A = pow(g, a_secret, p_small)

start = time.perf_counter()
recovered_a = brute_force_dlp(g, A, p_small)
elapsed_small = time.perf_counter() - start

print("=== Small Prime (p = 23) ===")
print(f"Intercepted A = {A}")
print(f"Eavesdropper recovered private key 'a': {recovered_a} (Time: {elapsed_small:.6f}s)")

# Case 2: Larger prime (Harder to brute force)
p_large = 10007
A_large = pow(g, a_secret, p_large)

start = time.perf_counter()
recovered_a_large = brute_force_dlp(g, A_large, p_large)
elapsed_large = time.perf_counter() - start

print("\n=== Larger Prime (p = 10007) ===")
print(f"Intercepted A = {A_large}")
print(f"Eavesdropper recovered private key 'a': {recovered_a_large} (Time: {elapsed_large:.6f}s)")
print(f"Brute force took {elapsed_large / elapsed_small:.2f}x longer.")