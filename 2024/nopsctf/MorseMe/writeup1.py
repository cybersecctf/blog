import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import os
def solve(morse):
 s=morse
 
 if os.path.exists(morse):
    with open(morse, "r+") as f:
       s=f.read()
 s=blog.solveup("morse",s) 
 if " " in s:
  n=2
  hex=" ".join([s[i:i+n] for i in range(0, len(s), n)])
 return blog.solveup("jojo1",s)
if __name__ == "__main__" :
 s=blog.set("challenge.txt",1)
 solve(s)