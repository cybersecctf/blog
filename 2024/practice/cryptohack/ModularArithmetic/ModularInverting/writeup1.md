<title>Modular Inverting-cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Modular Inverting-cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> As we've seen, we can work within a finite field Fp, adding and multiplying elements, and always obtain another element of the field.

For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p.

This is the multiplicative inverse of g.

Example: 7 * 8 = 56 ≡ 1 mod 11

What is the inverse element: 3 * d ≡ 1 mod 13?

 Think about the little theorem we just worked with. How does this help you find the inverse of an element?
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this is using extended gcd from       <a href="https://cybersecctf.github.io/blog/2024/practice/cryptohack/ModularArithmetic/egcd/writeup1.md">this</a>
problem  for calculate modular invert and get flag with this code
<pre>
#python
import blog
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
def solve(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
a = 3
if __name__ == "__main__" :
  a=blog.set(3,1)
  m = blog.set(13,2)
  d = solve(a, m)
  print(f"The value of d in the equation {a} * d ≡ 1 mod {m} and flag  is {d}")
</pre>
       flag is final result and d
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag"> 9
</p>
 
    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>


