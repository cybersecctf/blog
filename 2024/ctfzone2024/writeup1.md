 

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
#python conda activate   sage-env 
#sage
from sage.all import *
from Crypto.Util.number import long_to_bytes
from functools import namedtuple


def genM(A=2**1000):
    M = Matrix(QQ, [A*theta, 1, 0])
    M = M.stack(vector([R(A*2*pi), 0, 0]))
    M = M.stack(vector([A*w, 0, A]))
    return Matrix(QQ, M)


def convert(a2, a4, a6, Gx, Gy, Px, Py):
    x = R["x"].gen()
    f = x ** 3 + a2 * x ** 2 + a4 * x + a6
    roots = f.roots()

    # Singular point is a cusp.
    if len(roots) == 1:
        alpha = roots[0][0]
        u = (Gx - alpha) / Gy
        v = (Px - alpha) / Py
        return int(v / u)

    # Singular point is a node.
    if len(roots) == 2:
        if roots[0][1] == 2:
            alpha = roots[0][0]
            beta = roots[1][0]
        elif roots[1][1] == 2:
            alpha = roots[1][0]
            beta = roots[0][0]
        else:
            raise ValueError("Expected root with multiplicity 2.")

        t = (alpha - beta).sqrt()
        u = (Gy + t * (Gx - alpha)) / (Gy - t * (Gx - alpha))
        v = (Py + t * (Px - alpha)) / (Py - t * (Px - alpha))
        #print(f"{u= }")
        #print(f"{v = }")
        return u, v

    raise ValueError(f"Unexpected number of roots {len(roots)}.")


Point = namedtuple("Point", ["x", "y"])
R = RealField(prec=800)
P, Q = loads(open("output.dump", "rb").read())
u, v = convert(0, -3, -2, P.x, P.y, Q.x, Q.y)

theta = u.argument()
w = v.argument()

M = genM()
L = M.LLL()

print(long_to_bytes(abs(int(L[-1][1]))))
</pre>
python version
<pre>
import numpy as np
from sympy import symbols, sqrt, roots, re, im
from Crypto.Util.number import long_to_bytes
from collections import namedtuple

# Precision for floating point numbers
precision = 800
np.set_printoptions(precision=precision)

# Define named tuple for Points
Point = namedtuple("Point", ["x", "y"])

def genM(A=2**1000, u=None, v=None):
    M = np.array([[A*u, 1, 0],
                  [A*2*np.pi, 0, 0],
                  [A*v, 0, A]], dtype=np.float64)
    return M

def convert(a2, a4, a6, Gx, Gy, Px, Py):
    x = symbols('x')
    f = x**3 + a2 * x**2 + a4 * x + a6
    roots_ = roots(f)

    roots_list = list(roots_.keys())

    # Singular point is a cusp
    if len(roots_list) == 1:
        alpha = roots_list[0]
        u = (Gx - alpha) / Gy
        v = (Px - alpha) / Py
        return abs(u), abs(v)

    # Singular point is a node
    elif len(roots_list) == 2:
        alpha, beta = None, None

        for root, multiplicity in roots_.items():
            if multiplicity == 2:
                alpha = root
            else:
                beta = root

        if alpha is None or beta is None:
            raise ValueError("Expected root with multiplicity 2.")

        t = sqrt(re(alpha - beta))
        u = (Gy + t * (Gx - alpha)) / (Gy - t * (Gx - alpha))
        v = (Py + t * (Px - alpha)) / (Py - t * (Px - alpha))
        return abs(u), abs(v)

    raise ValueError(f"Unexpected number of roots {len(roots_list)}.")
def solve(P,Q):

 u, v = convert(0, -3, -2, P.x, P.y, Q.x, Q.y)
 # Directly use u and v as they are real numbers
 M = genM(u=u, v=v)
 # Perform LLL reduction using NumPy (this part needs a proper LLL implementation, which isn't directly available in NumPy)
 # Placeholder for LLL, assuming L is the result of LLL reduction
 L = np.linalg.qr(M)[0]  # Replace with proper LLL implementation
 # Print the result
 return long_to_bytes(abs(int(L[-1][1])))

if __name__ == "__main__" :
  P, Q = loads(open("output.dump", "rb").read())
  p=blog.set(P,1)
  q=blog.set(Q,2)
  print(solve(p,q))

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFZone{m4yb3_5h35_4_c0mpl3x_0n3}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on  elliptic curve discrete</p>

</body>
</html>
