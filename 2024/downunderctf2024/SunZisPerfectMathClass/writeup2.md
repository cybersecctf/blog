
def solve(n1,n2,n3,c1,c2,c3):
 from sympy import mod_inverse, integer_nthroot
 from Crypto.Util.number import long_to_bytes
 # Calculate N
 N = n1 * n2 * n3
 # Calculate N1, N2, N3
 N1 = N // n1
 N2 = N // n2
 N3 = N // n3
 # Calculate the modular inverses y1, y2, y3
 y1 = mod_inverse(N1, n1)
 y2 = mod_inverse(N2, n2)
 y3 = mod_inverse(N3, n3)
 # Use the Chinese Remainder Theorem to find x
 x = (c1 * N1 * y1 + c2 * N2 * y2 + c3 * N3 * y3) % N
 # Take the cube root of x
 m, exact = integer_nthroot(x, 3)
 flag = long_to_bytes(m).decode()
 return  flag
