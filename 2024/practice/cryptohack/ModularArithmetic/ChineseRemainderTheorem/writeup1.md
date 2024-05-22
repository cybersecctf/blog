
<!DOCTYPE html>
<html>

<body>
    <h1>Chinese Remainder - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers ai, and pairwise coprime integers ni, such that the following linear congruences hold:

 Note "pairwise coprime integers" means that if we have a set of integers {n1, n2, ..., ni}, all pairs of integers selected from the set are coprime: gcd(ni, nj) = 1.


x ≡ a1 mod n1
x ≡ a2 mod n2
...
x ≡ an mod nn


There is a unique solution x ≡ a mod N where N = n1 * n2 * ... * nn.

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.

Given the following set of linear congruences:

x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17


Find the integer a such that x ≡ a mod 935

 Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k*p for arbitrary integer k.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
run this code and get flag
<pre>
#python
from functools import reduce
import blog
def run(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p = prod/n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
    
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0,1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a , b = b, a%b
        x0, x1 = x1 -q*x0, x0
    if x1 < 0:
        x1 += b0
    return x1

a = [blog.set(2,1),blog.set(3,2),blog.set(5,3)] # x = a mod x
n = [blog.set(5,4),blog.set(11,5),blog.set(17,6)] # x = x mod n

print(a,n)
print(run(n,a))

</pre>       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">872
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on CHINESE REMAINDER THEOREM and mod inverse</p>
</body>
</html>

