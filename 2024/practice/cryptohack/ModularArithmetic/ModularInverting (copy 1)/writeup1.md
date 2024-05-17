#python
import sys
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
if len(sys.argv)>1:
  a=sys.argv[1]
m = 13
if len(sys.argv)>2:
  m=sys.argv[2]
d = mod_inverse(a, m)
print(f"The value of d in the equation 3 * d ≡ 1 mod 13 and flag  is {d}")