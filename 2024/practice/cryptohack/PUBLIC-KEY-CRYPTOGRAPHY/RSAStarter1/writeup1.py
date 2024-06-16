
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(a,b):
 return blog.solveup("find  two integers mod",a,b)
if __name__ == "__main__" :
 print(solve(pow(101,17),22663))
