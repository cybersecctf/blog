import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog

# Example AES encryption function for testing
def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, AES.block_size))

# Example AES decryption function for testing
def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

# Generate a random 16-byte AES key for testing
key = b'This is a key123'

# Example plaintext
plaintext = b'This is some data we want to encrypt.'

# Encrypt the plaintext using AES
ciphertext = aes_encrypt(key, plaintext)
 
# Precomputation Phase
def precompute_bicliques():
    # This function should generate bicliques for the attack
    # Placeholder for actual biclique computation
    bicliques = [np.random.rand(4, 4) for _ in range(10)]  # Random example bicliques
    return bicliques

# Online Phase: Match biclique to find the key
def match_biclique(ciphertext, known_plaintext, biclique):
    # Placeholder for matching logic
    # In a real attack, this function would perform complex computations to match biclique
    return np.random.choice([True, False])

# Key Recovery Phase
def recover_key(biclique):
    # Placeholder for key recovery logic
    # In a real attack, this would derive the key from the matched biclique
    return b'Recovered key!'

# Biclique Attack Function
def aes_biclique_attack(ciphertext, known_plaintext):
    # Precompute bicliques
    bicliques = precompute_bicliques()

    # Online phase: try to match bicliques
    for biclique in bicliques:
        if match_biclique(ciphertext, known_plaintext, biclique):
            # Recover the key if a match is found
            recovered_key = recover_key(biclique)
            return recovered_key
    
    # If no key is found
    return None
print(ciphertext)
# Example usage
def solve(operation,text,key):
  if operation=="encrypt":
     return aes_encrypt(key,text)
  elif operation=="decrypt":
     return aes_decrypt(key,text)
  else:
   ciphertext=key
   return aes_biclique_attack(ciphertext,text)
if __name__ == "__main__" :
 key=blog.set( b'This is a key123',1)
 text=blog.set( b'This is some data we want to encrypt.',2)
 print(solve("encrypt",key,text))