
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(p,q,n=None):
   if n==None:
    return p*q
   else:
    return n==p*q

if __name__ == "__main__" :
  p=blog.set(4391,1)
  q=blog.set(6659,2)
  n=blog.set(None,3)
  print(solve(p,q,n))
