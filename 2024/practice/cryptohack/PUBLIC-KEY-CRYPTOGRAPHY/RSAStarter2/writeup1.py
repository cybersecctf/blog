

import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog

def solve(m,e,p,q,n=-1):
  if n==-1:
      n= p*q
  return pow(m,e,n)
if __name__ == "__main__" :
 m=blog.set(12,1)#message
 e=blog.set(65537,4)
 p=blog.set(17,2)
 q=blog.set(23,3)
 n=blog.set(-1,4)
 print(solve(m,e,p,q,n))#not calulate m^e%n because large number
