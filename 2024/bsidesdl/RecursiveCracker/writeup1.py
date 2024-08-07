
#python
import os
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog




def solve(zipfile,dictionary):
 os.system("fcrackzip -v -D -u -p "+dictionary+" "+zipfile)
if __name__ == "__main__" :
  dictionary=blog.set(blog.solveup("garden","locate rockyou.txt",""))
  zipfile=blog.set("file.zip",1)
  solve(zipfile,dictionary)
