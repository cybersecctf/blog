#!/usr/local/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = os.urandom(16)  # Generate a random 16-byte key
cipher = AES.new(key, AES.MODE_ECB)  # Initialize the AES cipher in ECB mode

# Read the flag from the file
with open("flag.txt", "r") as f:
    flag = f.readline().strip()

# Pad the flag to a multiple of 16 bytes
flag_padded = pad(flag.encode(), 16)

# Encrypt the padded flag
flag_enc = cipher.encrypt(flag_padded)

print("Here's the encrypted flag in hex: ")
print(flag_enc.hex())
print("Alright, lemme spin up my Extremely Convenient Breaker (trademark copyright all rights reserved). ")

while True:
    ecb = input("What ciphertext do you want me to break in an extremely convenient manner? Enter as hex: ")
    try:
        ecb = bytes.fromhex(ecb)
        if not len(ecb) == 64:
            print("Sorry, it's not *that* convenient. Make your ciphertext 64 bytes please. ")
        elif ecb == flag_enc:
            print("No, I'm not decrypting the flag. ")
        else:
            print(cipher.decrypt(ecb))
    except Exception:
        print("Uh something went wrong, please try again. ")
