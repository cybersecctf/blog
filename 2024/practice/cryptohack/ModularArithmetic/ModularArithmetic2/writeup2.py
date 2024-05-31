#python  
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import gmpy2 
def solve (n ,tries=100) :
 a = gmpy2 .isqrt(n)
 c = 0
 while not gmpy2 . is_square (a **2 - n ) :
  a += 1
  c += 1
  if c > tries :
    return False
  bsq = a **2 - n
  b = gmpy2 . isqrt(bsq)
  p = a + b
  q = a - b
 return [ p , q ]

a=blog.set(5959,1)
print(solve(a,300))