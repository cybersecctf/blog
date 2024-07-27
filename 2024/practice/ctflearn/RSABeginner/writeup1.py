
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog


def solve(n,e,c):
    return blog.solveup("rsa",n,e,c)

if __name__ == "__main__" :
  e=3
  c=219878849218803628752496734037301843801487889344508611639028
  n= 245841236512478852752909734912575581815967630033049838269083
  print(solve(n,e,c))
