
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(text, key):
   return blog.solveup("vigenere cipher",text,key)

if __name__ == "__main__" :
  print(solve("nmivrxbiaatjvvbcjsf","secretkey"))
