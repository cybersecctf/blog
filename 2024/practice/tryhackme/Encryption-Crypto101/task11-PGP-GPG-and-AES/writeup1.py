
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(file,key ):
 blog.solveup("garden","unzip gpg_1593559828557.zip","$run")  
 blog.solveup("garden","gpg --import {key}","$run")
 blog.solveup("garden",f"gpgp {file}","$run")
 s=blog.solveup("garden","cat message","$run")
 return s
if __name__ == "__main__" :
  print(solve("message.gpg","tryhackme.key"))
