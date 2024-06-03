#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
def solve(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
a = 3
if __name__ == "__main__" :
  a=blog.set(3,1)
  m = blog.set(13,2)
  d = solve(a, m)
  print(f"The value of d in the equation {a} * d ≡ 1 mod {m} and flag  is {d}")