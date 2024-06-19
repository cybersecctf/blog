
#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
from factordb.factordb import FactorDB
def solve(n):

    f = FactorDB(n)
    f.connect()
    p,q = f.get_factor_list()
    return p,q



if __name__ == "__main__" :
 blog.islog=True
 n =blog.set( 510143758735509025530880200653196460532653147,1)
 s=solve(n)  
 print("flag is",min(s))
 
