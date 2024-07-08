
#python  
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import gmpy2
def solve(n,tries=100000):
     a = gmpy2.isqrt(n) + 1
     b2 = a*a - n
     while not gmpy2.is_square(b2):
        a += 1
        b2 = a*a - n
        tries -= 1
        if tries < 0:
            return None, None
     b = gmpy2.isqrt(b2)
     p = a + b
     q = a - b
     return int(p), int(q)
if __name__ == "__main__" :
   print(solve(341))
