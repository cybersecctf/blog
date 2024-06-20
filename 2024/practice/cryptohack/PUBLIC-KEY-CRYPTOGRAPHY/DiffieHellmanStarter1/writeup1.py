
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import sympy
def solve(p,g):

  return f"inverse element d such that {g} * d mod {p} = 1 is {pow(g, -1, p)}"
if __name__ == "__main__" :

 p=blog.set(991,1)
 g=blog.set(209,2)
 print( solve(p,g))
