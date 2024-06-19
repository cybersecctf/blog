
<!DOCTYPE html>
<html>

<body>
    <h1>RSA Starter 3- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> RSA relies on the difficulty of the factorisation of the modulus N. If the primes can be found then we can calculate the Euler totient of N and thus decrypt the ciphertext.

Given N = p*q and two primes:

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

What is the totient of N?

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
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
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">882564595536224140639625987657529300394956519977044270821168
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for introduce rsa encrypt and  modular exponentiation and pow mod</p>
</body>
</html>


