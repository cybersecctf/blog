#python
import sys
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Test the function

 
if __name__ == '__main__':
 a=blog.set(66528,1)

 
 b=blog.set(52920,2)  
 gcd, x, y = solve(a, b)
 print(gcd)
 print(blog.solveup("gcd",12,18))