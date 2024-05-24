#python
from collections.abc import Iterable

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

#one number
def square_root(p,n):
    for a in range(1, p):
        if (a*a) % p == n:
            print(f"The square root of {n} modulo {p} is {a}")
            break
    else:
        print(f"No square root found for {n} modulo {p}")

p = blog.set(29,1)
ints = blog.set("[14, 6, 11]",2)
type= blog.set("Quadratic residues full",2)


if not isinstance(ints, Iterable):
    ints = range(1, ints+1)
s= list(ints)
 

residues, non_residues = find_square_roots_modulo(p, ints)
q = []
if type=="square root":
 print("Quadratic residues and their square roots:")
for i, a in residues:
    q.append((-a % p, a))
    if type=="square root":
     print(f"{i} has square roots {a} and {-a % p}")

print("Quadratic residues full", set(q))
if type=="Quadratic non-residues":
 print("\nQuadratic non-residues:")
qn = [] 
for a in range(1,p):
    if not any(a == x[1] for x in q):
        qn.append(a)
if type=="Quadratic non-residues": 
   print(qn)
if type=="Quadratic residues full": 
  s=sorted(set([x[0] for x in q]))
  print(s,"flag is=",min(s))