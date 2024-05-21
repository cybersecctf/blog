
<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> your description
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> steps1 </li>
<pre>
def legendre_symbol(a, p):
    """
    Compute the Legendre symbol a|p using
    Euler's criterion. p is a prime, a is
    relatively prime to p (if p divides
    a, then a|p = 0)

    Returns 1 if a has a square root modulo
    p, -1 otherwise.
    """
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def square_root_modulo_p(a, p):
    """
    Find a square root of a modulo p. This
    algorithm applies when p = 3 (mod 4).
    """
    if legendre_symbol(a, p) != 1:
        return "a is not a quadratic residue modulo p"
    else:
        root = pow(a, (p + 1) // 4, p)
        return max(root, p - root)  # return the larger root

</pre>    
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>

