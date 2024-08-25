
#python
from Crypto.Util.number import inverse, long_to_bytes
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(n,e,c,p=0,q=0):
  if type(n)!="<class 'int'>":
    n=int(n)
  if type(e)!="<class 'int'>":
    e=int(e)
  if type(c)!="<class 'int'>":
    c=int(c)

  if p==0 and q==0: 
    p,q=blog.solveup("isprime",n)
  phi = (p-1)*(q-1)
  d = inverse(e, phi)
  m = pow(c,d,n)
  return long_to_bytes(m)
if __name__ == "__main__" :
 n = blog.set(831416828080417866340504968188990032810316193533653516022175784399720141076262857,1)
 e = blog.set(65537,2)
 c =blog.set( 240986837130071017759137533082982207147971245672412893755780400885108149004760496,3)
 p = blog.set(1593021310640923782355996681284584012117,4)
 q = blog.set(521911930824021492581321351826927897005221,5)
 print(solve(n,e,c,p,q))
