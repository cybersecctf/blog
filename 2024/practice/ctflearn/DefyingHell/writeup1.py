
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import math;
from sympy.ntheory.residue_ntheory import discrete_log

def solve(p,g,A,B):
 
 x = discrete_log(p, A, 2)
 y = discrete_log(p, B, 2)

 if (pow(2,x,p) == A):
    a = x

 if (pow(2,y,p) == B):
    
    b = y
 k_a = pow(B,a,p)
 k_b = pow(A,b,p)
 k = k_a # Note that k = k_a = k_b

 a=bytes.fromhex(hex(a)[2:])
 b=bytes.fromhex(hex(b)[2:])
 return a,b
if __name__ == "__main__" :
 p =blog.set( 2468642135797531,1)
 g = blog.set(2,2)
 A =blog.set( 679217732839784,3)# A = g^{a} mod p where a is the secret integer of Alice
 B =blog.set( 1255037608816496,4) # B = g^{b} mod p where b is the secret integer of Bob
 print(solve(p,g,A,B))
