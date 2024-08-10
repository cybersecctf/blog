
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import os,subprocess
def solve(term, file="sol.json"):
    return blog.solveup("search json",term,file)
if __name__ == "__main__" :
  print(solve("Should you trust DES? Yea/Nay"))
  print(solve("What was the result of the attempt to make DES more secure so that it could be used for longer?"))
  print(solve("Is it ok to share your public key? Yea/Nay"))

