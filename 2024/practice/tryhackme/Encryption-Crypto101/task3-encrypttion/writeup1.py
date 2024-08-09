
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve( search,file):

   return blog.solveup("search json",search,file)

if __name__ == "__main__" :
  print(solve("What does SSH stand for?","sol.json"))
  print(solve("How do webservers prove their identity?","sol.json"))
  print(solve("What is the main set of standards you need to comply with if you store or process payment card details?","sol.json"))
