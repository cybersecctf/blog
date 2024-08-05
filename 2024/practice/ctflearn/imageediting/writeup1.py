
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(file, search=""):
    try:
        # Run stegsolve command
        if search=="stegsolve" or search=="":
         blog.solveup("garden","java -jar stegsolve.jar","")#analysis  data extract  options in pic
         if search=="":
           return
        result=blog.solveup("garden",f"zsteg {file}","")#analysis  data extract  options in pic
        print(result)
        
    except Exception as e:
        print(f"Error running zsteg: {e}")
   

if __name__ == "__main__" :
 file="writeup1.png" 
 solve(file,"stegsolve")

 solve(file,"zsteg")
 #extract_binwalk(file)
