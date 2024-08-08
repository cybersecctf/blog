
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(url, search=""):
     s=blog.solveup("inspect",url+"/robots.txt","/")
     d=s.replace("Disallow: ","")
     d="https://ctflearn.com"+d.strip()
     
     print(d)
     s=blog.solveup("inspect",d,search)
    
     return s

if __name__ == "__main__" :
  s=solve("https://ctflearn.com/","{")
  
  
  print(s)
