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
def solve (n ,tries=100) :
 a = gmpy2 .isqrt(n)
 c = 0
 while not gmpy2 . is_square (a **2 - n ) :
  a += 1
  c += 1
  if c > tries :
    return False
  bsq = a **2 - n
  b = gmpy2 . isqrt(bsq)
  p = a + b
  q = a - b
 return [ p , q ]

a=blog.set(5959,1)
print(solve(a,300))    
</pre>
        
    
    </ol>
<br> 
    <h2>Flag</h2>
    <p class="flag">1
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for find factors  of small n with   Fermat</p>
</body>
</html>

