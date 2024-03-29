# Plaintexts and Ciphertexts
plaintext1 = 12
ciphertext1 = 0x5004
plaintext2 = 23
ciphertext2 = 0x6e4b

# Recover the first part of the key
key_part1 = plaintext1 ^ ciphertext1

 
print(key_part1)
# Encrypted flag
encrypted_flag = 0x5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b

# Decrypt the flag using the full key
decrypted_flag = encrypted_flag ^ key_part1

# Print the decrypted flag
print("Decrypted Flag:",hex(decrypted_flag))
  