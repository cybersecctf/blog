
<!DOCTYPE html>
<html>

<body>
    <h1>RSA Starter 4- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> The private key d is used to decrypt ciphertexts created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).

The private key is the secret piece of information or "trapdoor" which allows us to quickly invert the encryption function. If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to first factorise the modulus.

In RSA the private key is the modular multiplicative inverse of the exponent e modulo the totient of N.

Given the two primes:

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

and the exponent:

e = 65537

What is the private key d?

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
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
</pre>        
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">13371337
</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for introduce rsa decrypt with n e c</p>
</body>
</html>