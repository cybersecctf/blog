
<!DOCTYPE html>
<html>

<body>
    <h1>Diffie-Hellman Starter 2 - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> Every element of a finite field Fp can be used to make a subgroup H under repeated action of multiplication. In other words, for an element g: H = {g, g^2, g^3, ...}

A primitive element of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n. Because of this, primitive elements are sometimes called generators of the finite field.

For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp.

This problem can be solved by brute-force, but there's also clever ways to speed up the calculation.
 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
for get flag run this code if blog.solveup("isprine",n) not working use site and get primefactor list of n and calculate phi and then get flag with run this code
<pre>
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import sympy
def is_generator(k, p):
  for n in range(2, p):
    if pow(k, n, p) == k:
      return False
  return True
def solve(p):
 for k in range(p):
  if is_generator(k, p):
     return k
if __name__ == "__main__" :

 p=blog.set(28151,1)
 print( solve(p))
</pre>
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">7</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for decrypt message with n that e is small like 3</p>
</body>
</html>






