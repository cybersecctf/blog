

<!DOCTYPE html>
<html>

<body>
    <h1>Quadratic Residues-  cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo p = 29. We can take the integer a = 11 and calculate a2 = 5 mod 29.

As a = 11, a2 = 5, we say the square root of 5 is 11.

This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a2 = 18

Your first idea might be to start with a = 1 and loop to a = p-1. In this discussion p isn't too large and we can quickly look.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a ∈ Fp* you never find an a such that a2 = 18.

What we are seeing, is that for the elements of F*p, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp*, there is no square root.

We say that an integer x is a Quadratic Residue if there exists an a such that a2 = x mod p. If there is no such solution, then the integer is a Quadratic Non-Residue.


In other words, x is a quadratic residue when it is possible to take the square root of x modulo an integer p.

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

If a2 = x then (-a)2 = x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.


p = 29
ints = [14, 6, 11]
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 
<pre>
#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog

def find_square_roots_modulo(p, ints):
    residues = []
    non_residues = []
    for a in range(1, p):
        for i in ints:
            if (a*a) % p == i:
                residues.append((i, a))
                break
        else:
            non_residues.append(a)
    return residues, non_residues
import sys
#one number
def square_root(p,n):
 for a in range(1, p):
    if (a*a) % p == n:
        print(f"The square root of {n} modulo {p} is {a}")
        break
    else:
           print(f"No square root found for {n} modulo {p}")
p=blog.setval(29,1)
ints =blog.setval( "[14, 6, 11]",2)

residues, non_residues = find_square_roots_modulo(p, ints)

print("Quadratic residues and their square roots:")
for i, a in residues:
    print(f"{i} has square roots {a} and {-a % p}")

print("\nQuadratic non-residues:")
for a in non_residues:
    print(a)
qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")
</pre>
       
    and flag is result
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">8
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on Quadratic Residues and square root</p>
</body>
</html>

