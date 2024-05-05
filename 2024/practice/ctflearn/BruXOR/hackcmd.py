from itertools import cycle
import sys

def xor_brute_force(ciphertext, search, key_length):
    # Generate all possible keys
    keys = [bytes([i]) * key_length for i in range(256)]
    
    for key in keys:
        plaintext = ''.join(chr(c ^ k) for c, k in zip(ciphertext.encode(), cycle(key)))
        if plaintext.startswith(search):
            print(f"Key: {key}, Message: {plaintext}")

ciphertext = "q{vpln'bH_varHuebcrqxetrHOXEj"
search = 'flag'
key_length = 1  # replace with your key length

if len(sys.argv) > 1:
    ciphertext = sys.argv[1]
if len(sys.argv) > 2:
    search = sys.argv[2]
if len(sys.argv) > 3:
    key_length = int(sys.argv[3])  # convert argument to integer

xor_brute_force(ciphertext, search, key_length)
