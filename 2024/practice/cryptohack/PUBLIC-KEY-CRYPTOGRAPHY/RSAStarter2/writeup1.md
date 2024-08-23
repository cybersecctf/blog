<title>RSA Starter 2- cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>RSA Starter 2- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> RSA encryption is modular exponentiation of a message with an exponent e and a modulus N which is normally a product of two primes: N = p * q.

Together the exponent and modulus form an RSA "public key" (N, e). The most common value for e is 0x10001 or 65537.

"Encrypt" the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23. What number do you get as the ciphertext?

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
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
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">301
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for introduce rsa encrypt and  modular exponentiation and pow mod</p>
</body>
</html>


