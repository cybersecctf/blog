<title>RSA Starter 4- cryptohack</title>

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
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(e, phi):
    if  blog.solveup("gcd",e, phi)[0] != 1:
        return None  # No mod inverse if e and phi are not coprime

    # Extended Euclidean Algorithm to find modular inverse
    old_r, r = e, phi
    old_s, s = 1, 0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    return old_s % phi

# Example usage:
p = blog.set(61,1)  # Replace with your chosen prime number
q =blog.set( 53,2)  # Replace with your chosen prime number
n = blog.set(p * q,3)
phi = blog.solveup("totient",n,p,q)
e = 17  # Replace with your chosen public exponent

d = solve(e, phi)
print(f"The private key d is: {d}")
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


