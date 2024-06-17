
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(m,e,n=-1,p=-1,q=-1):
 if n==-1:
   n=p*q
 return pow(m,e,n)
if __name__ == "__main__" :
 m=blog.set(12,1)
 n=blog.set(-1,2)
 e=0
 if n==-1:
  p=blog.set(17,3)
  q=blog.set(23,4)
  n=p*q
  e=blog.set(65537,5)
 else:
  e=blog.set(65537,3)
 print(solve(m,e,n,p,q))
