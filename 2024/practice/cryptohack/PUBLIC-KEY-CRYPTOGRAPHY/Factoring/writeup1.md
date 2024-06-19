
<!DOCTYPE html>
<html>

<body>
    <h1>Factoring - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> So far we've been using the product of small primes for the modulus, but small primes aren't much good for RSA as they can be factorised using modern methods.

What is a "small prime"? There was an RSA Factoring Challenge with cash prizes given to teams who could factorise RSA moduli. This gave insight to the public into how long various key sizes would remain safe. Computers get faster, algorithms get better, so in cryptography it's always prudent to err on the side of caution.

These days, using primes that are at least 1024 bits long is recommended—multiplying two such 1024 primes gives you a modulus that is 2048 bits large. RSA with a 2048-bit modulus is called RSA-2048.

Some say that to really remain future-proof you should use RSA-4096 or even RSA-8192. However, there is a tradeoff here; it takes longer to generate large prime numbers, plus modular exponentiations are predictably slower with a large modulus.

Factorise the 150-bit number 510143758735509025530880200653196460532653147 into its two constituent primes. Give the smaller one as your answer.

Resources:
  - How big an RSA key is considered secure today?
  - primefac-fork
 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
#python
import blog
from factordb.factordb import FactorDB
def solve(n):
    f = FactorDB(n)
    f.connect()
    factors = f.get_factor_list()
    if len(factors) == 1 and factors[0] == n:
        # The number is prime
     
        return "isprime"
    else:
        # The number is composite; return its factors
        return factors



if __name__ == "__main__" :
 n =blog.set( 510143758735509025530880200653196460532653147,1)
 s=solve(n)  

 print("flag is",min(s))
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">19704762736204164635843
</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for factorize supported number and print minimum</p>
</body>
</html>

