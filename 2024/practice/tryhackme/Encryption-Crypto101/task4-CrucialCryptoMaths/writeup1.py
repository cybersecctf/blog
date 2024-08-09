
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(a, b):
   return a%b

if __name__ == "__main__" :
 print(solve(30,5))
 print(solve(25,7))
 print(solve(118613842,9091))
