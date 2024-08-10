 

<!DOCTYPE html>
<html>
 
<body>
    <h1>ctfzone2024---Shes the Real one  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  I can trust her with my life.

<a href="https://cybersecctf.github.io/blog/2024/ctfzone2024/shes-the-real-one.zip.9296652663e664cb8042d54c718e7be6">link text</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is a  elliptic curve discrete that should get p ,q,e with reverse saga 
and solve it with bruteforce or other method
get p , q e by urself
<pre>
import blog
from sage.all import *
import random

def solve(P, Q, E):
    
    try:
        assert P == E((P[0], P[1]))
    except TypeError:
        print "[-] Point does not lie on the curve"
        return -1

    res = 2*P
    if res == Q:
        return 2
    if Q == E((0, 1, 0)):
        return _order
    if Q == P:
        return 1
    i = 3
    while i <= P.order() - 1:
        res = res + P
        if res == Q:
            return i
        i += 1
    return -1


if __name__ == "__main__":
    E = blog.set(0,1)
    P = blog.set(0,2)
    Q=blog.set(0,3)
    try:
        for _ in range(100):
            x = random.randint(2, 18)
            assert solve(E((5, 1)), x*P, E) == x
    except Exception as e:


</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on  elliptic curve discrete</p>

</body>
</html>
