
from itertools import cycle
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

def solve(ciphertext, search, key_length):
    # Generate all possible keys
    keys = [bytes([i]) * key_length for i in range(256)]
    
    for key in keys:
        plaintext = ''.join(chr(c ^ k) for c, k in zip(ciphertext.encode(), cycle(key)))
        if plaintext.startswith(search):
            return f"Key: {key}, Message: {plaintext}"
    return "flag not found"
if __name__ == "__main__" :
 ciphertext = blog.set("q{vpln'bH_varHuebcrqxetrHOXEj",1)
 search = blog.set('flag',2)
 key_length = blog.set(1,3)  # replace with your key length
 print(solve(ciphertext, search, key_length))

