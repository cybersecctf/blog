# Given plaintext and ciphertext pairs
plaintext1 = 12
ciphertext1 = 0x5004
plaintext2 = 23
ciphertext2 = 0x6e4b

# Solve for the key
key = ciphertext1 ^ plaintext1
print("Key for plaintext1 =", key)

# Verify the key with the second pair
if ciphertext2 == (plaintext2 ^ key):
    print("Key is correct:", key)
else:
    print("Key is incorrect.")
