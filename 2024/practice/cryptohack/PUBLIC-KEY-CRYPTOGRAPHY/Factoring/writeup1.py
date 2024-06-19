
#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
from factordb.factordb import FactorDB
def solve(n):
    blog.log("factoring...")
    f = FactorDB(n)
    f.connect()
    factors = f.get_factor_list()
    if len(factors) == 1 and factors[0] == n:
        # The number is prime
     
        return "isprime"
    else:
        # The number is composite; return its factors
        blog.log(f"factors{factors}")          
        return factors



if __name__ == "__main__" :
 n =blog.set( 510143758735509025530880200653196460532653147,1)
 s=solve(n)  

 print("flag is",min(s))
 
