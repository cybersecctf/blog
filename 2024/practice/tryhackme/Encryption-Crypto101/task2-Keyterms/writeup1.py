
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def search_json(term,file):
    a=blog.set(file,1)
  
    if term=="":
         return a
    return a.get(term, "Term not found")

def solve( file,search="Cryptanalysis"):
    return search_json(file,search)
   
     
if __name__ == "__main__" :
  print(solve("Are SSH keys protected with a passphrase or a passwor?","sol.json"))
