import hashlib

def hash_file(filepath, chunk_size=4096):
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            sha1.update(chunk)
            sha256.update(chunk)

    return sha1.hexdigest(), sha256.hexdigest()

# Example usage (Replace with your own filename)
file_path = "test.txt"

# Creating a test file first
with open(file_path, "w") as f:
    f.write("Cryptography and Network Security Lab 10 File Hashing Test")

sha1_digest, sha256_digest = hash_file(file_path)
print("File SHA-1  :", sha1_digest)
print("File SHA-256:", sha256_digest)