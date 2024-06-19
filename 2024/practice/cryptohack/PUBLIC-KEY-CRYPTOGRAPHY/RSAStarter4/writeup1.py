
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(e, phi):
    if  blog.solveup("gcd",e, phi)[0] != 1:
        return None  # No mod inverse if e and phi are not coprime

    # Extended Euclidean Algorithm to find modular inverse
    old_r, r = e, phi
    old_s, s = 1, 0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    return old_s % phi

# Example usage:
p = blog.set(61,1)  # Replace with your chosen prime number
q =blog.set( 53,2)  # Replace with your chosen prime number
n = blog.set(p * q,3)
phi = blog.solveup("totient",n,p,q)
e = 17  # Replace with your chosen public exponent

d = solve(e, phi)
print(f"The private key d is: {d}")
 
