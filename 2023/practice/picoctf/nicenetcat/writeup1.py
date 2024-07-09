
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import os
def solve(x):
 if os.path.exists(x):
  x=open(x).read().strip()
 s=''.join(chr(int(s)) for s in x.split())
 return s
if __name__ == "__main__" :
 print(solve("flag"))
 print(solve("65 78"))#test execute
