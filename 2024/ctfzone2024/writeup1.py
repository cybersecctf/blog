
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
from sage.all import *
import random
# sage
from functools import namedtuple
Point = namedtuple("Point", ["x", "y"])
P, Q = loads(open("output.dump", "rb").read())
print(P, Q)
def solve(P, Q, E):
    
    try:
     assert P == E((P[0], P[1]))
    
       

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
    except :
        return "[-] Point does not lie on the curve"

E=blog.set(0,1)
P = blog.set(0,2)
Q=blog.set(0,3)
try:
        for _ in range(100):#manual change if not working in this problem
            x = random.randint(2, 18)
            assert solve(E((5, 1)), x*P, E) == x
except Exception as e:
        print(str(e))


