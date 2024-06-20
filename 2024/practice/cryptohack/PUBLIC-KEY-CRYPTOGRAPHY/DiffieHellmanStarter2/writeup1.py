
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import sympy
def is_generator(k, p):
  for n in range(2, p):
    if pow(k, n, p) == k:
      return False
  return True
def solve(p):
 for k in range(p):
  if is_generator(k, p):
     return k
                             
       
   
if __name__ == "__main__" :

 p=blog.set(28151,1)
 print( solve(p))
