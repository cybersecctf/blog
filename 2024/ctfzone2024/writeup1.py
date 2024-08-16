
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
