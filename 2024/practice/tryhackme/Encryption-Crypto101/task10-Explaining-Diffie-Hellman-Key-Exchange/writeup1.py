
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import random

import os,subprocess
def solve(p, g):
 # Prime number and primitive root
 P = 23
 G = 5
 # Alice's private key
 a = random.randint(1, P-1)
 # Bob's private key
 b = random.randint(1, P-1)
 # Alice's public key
 A = pow(G, a, P)
 # Bob's public key
 B = pow(G, b, P)
 # Shared secret key
 shared_key_Alice = pow(B, a, P)
 shared_key_Bob = pow(A, b, P)
 return a,b,A,B,shared_key_Alice,shared_key_Bob



if __name__ == "__main__" :
  p=blog.set(23,1)
  g=blog.set(5,2)
  print(solve(p,g))
