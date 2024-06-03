<!DOCTYPE html>
<html>

<body>
    <h1>small  n to pq with fermat - cryptohack</h1>
 
    <h2>Challenge Description</h2>
    <p> We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.

 this is easy method for find pq from n in in n=p*q
</p> 
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this is working when p and q are close enough(shouldn't  exceeds  tries )
<pre>
#python  
import blog
import gmpy2
def solve(n,tries=100000):
     a = gmpy2.isqrt(n) + 1
     b2 = a*a - n
     while not gmpy2.is_square(b2):
        a += 1
        b2 = a*a - n
        tries -= 1
        if tries < 0:
            return None, None
     b = gmpy2.isqrt(b2)
     p = a + b
     q = a - b
     return int(p), int(q)
if __name__ == "__main__" :
   print(solve(341))
</pre>
        
    
    </ol>
<br> 
    <h2>Flag</h2>
    <p class="flag">[mpz(101), mpz(59)]
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for find factors  of small n with   Fermat</p>
</body>
</html>

