
#python
import string, itertools

import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
 #create map repeating or ciustom like mapping 1 below for this quetion
def create_mapping(i):
    # Generate all possible 5-letter combinations of 'A' and 'B'
    combinations = [''.join(combination) for combination in itertools.product('AB', repeat=i)]
    
    # Map each combination to a letter in the alphabet
    mapping = {combination: letter for combination, letter in zip(combinations, string.ascii_uppercase)}
    
    return mapping
def bacon_decrypt(ciphertext, mapping):
    # Split the ciphertext into chunks of 5 characters (since Bacon's cipher uses 5-bit binary codes)
    chunks = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
    
    # Decrypt the ciphertext using the provided mapping
    plaintext = ''.join(mapping.get(chunk, '?') for chunk in chunks)
    
    return plaintext

def solve(ciphertext,mapping=-1):
 s=[]
 
 mapping1 = {'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABABA': 'L', 'ABBAA': 'N', 'ABBAB': 'O', 'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'T', 'BAABB': 'U', 'BABBB': 'X', 'BABBA': 'Y', 'ABBBA': 'M', 'BBBBA': 'S', 'AABBA': 'V', 'BABBB': 'W', 'BBBB': 'Z'}
 if mapping==-1:
  s.append(bacon_decrypt(ciphertext,mapping1))
   
  for i in range(20):
   d= bacon_decrypt(ciphertext,create_mapping(i))
   if d.count('?')!=len(d):
     s.append(d)
 else:
   s.append( bacon_decrypt(ciphertext,mapping))
 return s

# Your Bacon-encoded ciphertext
ciphertext =blog.set('ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB',1)  # Replace with your actual ciphertext
print(solve(ciphertext))

