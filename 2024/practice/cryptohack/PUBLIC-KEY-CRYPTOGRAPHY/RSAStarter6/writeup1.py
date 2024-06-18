
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
from factordb.factordb import FactorDB

def solve(n,e,c):
 phi = blog.solveup("phi",n)#calculate phi of n for factordb supported numbers in python
 d = pow(e, -1, phi)
 return pow(c, d, n)
if __name__ == "__main__" :
  n=882564595536224140639625987659416029426239230804614613279163
  f = FactorDB(n)
  f.connect()
  p,q = f.get_factor_list()
  e = 65537
  c = 77578995801157823671636298847186723593814843845525223303932     
  print(solve(n,e,c))
