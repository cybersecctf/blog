import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(a, p):
    return pow(a, p - 1, p)  
 
# Test the function with your number and a prime
if __name__ == "__main__" :
 a=blog.set(273246787654,1)
 p=blog.set(17,2) 
 print(solve(a, p))