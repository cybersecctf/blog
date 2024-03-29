from pwn import *

# Connect to the remote server
p = remote("mercury.picoctf.net", 20266)

# Receive the welcome message and encrypted flag
print(p.recvuntil(b'flag!\n'))
encrypted_flag = p.recvline().strip()
print("Flag:", encrypted_flag)

# Send your first data to encrypt (e.g., 12)
p.sendline(b'12')

# Receive the encrypted data (e.g., 5004)
print(p.recvuntil(b'Here ya go!\n'))
ciphertext1 = p.recvline().strip()

# Send your second data to encrypt (e.g., 23)
p.sendline(b'23')

# Receive the encrypted data (e.g., 6e4b)
print(p.recvuntil(b'Here ya go!\n'))
ciphertext2 = p.recvline().strip()

print("Result 1:", ciphertext1)
print("Result 2:", ciphertext2)

# Convert the plaintexts and ciphertexts to integers
plaintext1 = 12
ciphertext1 = int(ciphertext1, 16)
plaintext2 = 23
ciphertext2 = int(ciphertext2, 16)
print("Result 1:", ciphertext1)

print("Result 2:", ciphertext2)
# Attempt key recovery
key_candidate = bytes([plaintext1 ^ (ciphertext1 & 0xFF)])

# Confirm the key by XOR-ing with the second plaintext-ciphertext pair
if bytes([plaintext2 ^ (ciphertext2 & 0xFF)]) == key_candidate:
    print("Recovered Key:", key_candidate)
else:
    print("Key recovery failed.")
