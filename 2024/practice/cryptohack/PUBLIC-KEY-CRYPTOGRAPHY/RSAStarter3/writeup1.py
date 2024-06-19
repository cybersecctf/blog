
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
from factordb.factordb import FactorDB
def solve(n,p=-1,q=-1):
  blog.log("if n=-1 n=p*q solve(n,p,q)")
  if p==-1 and q==-1:
    f = FactorDB(n)
    f.connect()
    p,q = f.get_factor_list()
    print(p,q)
  count=(p-1)*(q-1)    
  return count
if __name__ == "__main__" :
 n=blog.set(-1,1)
 p = blog.set(857504083339712752489993810777,2)
 q = blog.set(1029224947942998075080348647219,3)
 n=p*q
 print(solve(n,p,q)) 
