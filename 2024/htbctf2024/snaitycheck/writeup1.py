
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(url, search=""):

  blog.solveup("inspect",url,search) 

if __name__ == "__main__" :
  print(solve("https://94.237.49.212:52765/"))
