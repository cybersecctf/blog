from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
# Simulate encryption (for demonstration purposes)
key = os.urandom(16)
cipher = AES.new(key, AES.MODE_ECB)

# Target ciphertext (you need to get this from the challenge)
target_ciphertext = cipher.encrypt(pad(b"lactf{example_flag_here}", 16))

# Guess the flag block by block
block_size = 16
known_flag = "lactf{"
while not known_flag.endswith("}"):
    padding_length = block_size - (len(known_flag) % block_size) - 1
    padding = "A" * padding_length
    known_block = (padding + known_flag).encode()

    # Encrypt and compare outputs
    encrypted_block = cipher.encrypt(pad(known_block, block_size))[:block_size]
    for i in range(32, 127):  # Printable ASCII
        test_block = (padding + known_flag + chr(i)).encode()
        test_cipher = cipher.encrypt(pad(test_block, block_size))[:block_size]
        print(i,test_cipher,test_block)
        if test_cipher == encrypted_block:
            known_flag += chr(i)
            print(f"Discovered so far: {known_flag}")
            break
