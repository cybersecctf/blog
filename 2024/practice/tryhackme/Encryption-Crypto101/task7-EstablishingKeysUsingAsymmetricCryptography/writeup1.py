
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve():
   blog.solveup("inspect","https://robertheaton.com/2014/03/27/how-does-https-actually-work/","")
   return "complete"

if __name__ == "__main__" :
  print(solve())
