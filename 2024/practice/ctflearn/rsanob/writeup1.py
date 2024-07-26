
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(n,e,c):
 return blog.solveup("rsa",n,e,c)
e= 1
c=9327565722767258308650643213344542404592011161659991421
n= 245841236512478852752909734912575581815967630033049838269083
print(solve(n,e,c))
