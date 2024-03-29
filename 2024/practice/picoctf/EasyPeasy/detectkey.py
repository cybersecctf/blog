# Given plaintext and ciphertext pairs
plaintext1 = 12
ciphertext1 = 0x5004
plaintext2 = 23
ciphertext2 = 0x6e4b

# Iterate over possible key values
for key in range(0, 65536):  # Assuming the key space is within 16 bits (0 to 65535)
    # Verify if the key produces correct ciphertext for both plaintext-ciphertext pairs
    if ciphertext1 == (plaintext1 ^ key) and ciphertext2 == (plaintext2 ^ key):
        print("Correct key found:", key)
        break
else:
    print("Unable to find the correct key.")
