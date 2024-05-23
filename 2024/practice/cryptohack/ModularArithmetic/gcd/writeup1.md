
<!DOCTYPE html>
<html>

<body>
    <h1>Greatest Common Divisor- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).

For a = 12, b = 8 we can calculate the divisors of a: {1,2,3,4,6,12} and the divisors of b: {1,2,4,8}. Comparing these two, we see that gcd(a,b) = 4.

Now imagine we take a = 11, b = 17. Both a and b are prime numbers. As a prime number has only itself and 1 as divisors, gcd(a,b) = 1.

We say that for any two integers a,b, if gcd(a,b) = 1 then a and b are coprime integers.

If a and b are prime, they are also coprime. If a is prime and b < a then a and b are coprime.

Think about the case for a prime and b > a, why are these not necessarily coprime?


There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.

Try coding it up; it's only a couple of lines. Use a = 12, b = 8 to test it.

Now calculate gcd(a,b) for a = 66528, b = 52920 and enter it below.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we run this code for get gcd with Euclid's Algorithm non recursive method on python
<pre>
#python
import sys
import blog
def run(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Test the function

 

if __name__ == '__main__':
 a=blog.set(66528,1)

 
 b=blog.set(52920,2)  
 gcd, x, y = run(a, b)
 print(gcd)
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">1512
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for  get gcd with Euclid's Algorithm non recursive method on pythons</p>
</body>
</html>

