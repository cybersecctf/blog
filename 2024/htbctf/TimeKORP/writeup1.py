
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(file, search=""):
   blog.islog=True
   rock=blog.solveup("garden","locate rockyou.txt","")
   result=blog.solveup("garden",f"sudo  zip2john -o {file} > zip.hash","")
   return result 

if __name__ == "__main__" :
  print(solve("web_timecorp.zip"))
