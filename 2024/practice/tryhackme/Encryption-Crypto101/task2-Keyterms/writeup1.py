
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def search_json(term,file="def.json"):
    a=blog.set("def.json",1,"file")
    return a.get(term, "Term not found")

def solve( search="Cryptanalysis"):
    return search_json(search)
   
     
if __name__ == "__main__" :
  print(solve("Alice and Bob"))
