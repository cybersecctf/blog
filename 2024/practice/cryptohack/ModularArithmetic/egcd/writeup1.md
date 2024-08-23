<title>Extended GCD- cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Extended GCD- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> Let a and b be positive integers.

The extended Euclidean algorithm is an efficient way to find integers u,v such that

a * u + b * v = gcd(a,b)

 Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.


Using the two primes p = 26513, q = 32321, find the integers u,v such that

p * u + q * v = gcd(p,q)
<pre>
import blog
p = 26513
q = 32321
print(blog.solveup("egcd",p,q))
</pre>
Enter whichever of u and v is the lower number as the flag.

 Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
we run this code for get extened gcd with Euclidean algorithm non recursive method
    <ol>
<pre>
#python
import blog
def solve(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Test the function

a = blog.set(26513,1)
b =blog.set( 32321,2)
gcd, x, y = solve(a, b)
print(x,y)
</pre>
flag is value that is smallest       because print(10245*26513+ -8404*32321) is 1
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">-8404
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for work on extened gcd with Euclidean algorithm non recursive method</p>
</body>
</html>

