<title>Diffie-Hellman Starter 1 - cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Diffie-Hellman Starter 1 - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>The set of integers modulo n, together with the operations of both addition and multiplication is a ring. This means that adding or multiplying any two elements in the set returns another element in the set.

When the modulus is prime: n = p, we are guaranteed an inverse of every element in the set, and so the ring is promoted to a field. We refer to this field as a finite field Fp.

The Diffie-Hellman protocol works with elements of some finite field Fp, where the prime modulus is typically a large prime.

Given the prime p = 991, and the element g = 209, find the inverse element d such that g * d mod 991 = 1.

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
for get flag run this code if blog.solveup("isprine",n) not working use site and get primefactor list of n and calculate phi and then get flag with run this code
<pre>
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import sympy
def solve(p,g):

  return pow(g, -1, p)

   
if __name__ == "__main__" :

 p=blog.set(991,1)
 g=blog.set(209,2)
 print( solve(p,g))
</pre>
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{N33d_m04R_p4dd1ng}</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for decrypt message with n that e is small like 3</p>
</body>
</html>






