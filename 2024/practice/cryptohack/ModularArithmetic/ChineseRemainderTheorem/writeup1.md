
<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

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
import blog
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m

# Given congruences
N = blog.set(935,1)
N1 = blog.set(5,2)
N2 = blog.set(11,3)
N3= blog.set(17,4)

N1, N2, N3 = N3*N2,N1*N3,N1*N2
y1, y2, y3 = mod_inverse(N1, 5), mod_inverse(N2, 11), mod_inverse(N3, 17)

# Calculate a_i values
a1 = (2 * N1 * y1) % N
a2 = (3 * N2 * y2) % N
a3 = (5 * N3 * y3) % N

# Compute x
x = (a1 + a2 + a3) % N
print(f"The integer a such that x ≡ a mod 935 is: {x}")

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

