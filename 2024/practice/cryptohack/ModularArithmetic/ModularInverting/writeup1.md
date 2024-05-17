
<!DOCTYPE html>
<html>

<body>
    <h1>Modular Inverting- Modular Inverting</h1>

    <h2>Challenge Description</h2>
    <p> As we've <a href="https://cybersecctf.github.io/blog/2024/practice/cryptohack/ModularArithmetic/ModularArithmetic2/writeup1.md">seen</a>, we can work within a finite field Fp, adding and multiplying elements, and always obtain another element of the field.

For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p.

This is the multiplicative inverse of g.

Example: 7 * 8 = 56 ≡ 1 mod 11

What is the inverse element: 3 * d ≡ 1 mod 13?

 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 this is problem using modulainverting  q with <a href="https://cybersecctf.github.io/blog/2024/practice/cryptohack/ModularArithmetic/ModularArithmetic2/writeup1.md">extended gcd</a>
       for find number and flag 
<pre>
#python
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
a = 3
m = 13
d = mod_inverse(a, m)
print(f"The value of d in the equation 3 * d ≡ 1 mod 13 and flag  is {d}")
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">9
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on Modular inverse  and extended gcd </p>
</body>
</html>


