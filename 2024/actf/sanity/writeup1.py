import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog#use blog.py in https://cybersecctf.github.io/blog
def solve(word):
  blog.solveup("reverse string",word)#reverse challenge description here
if __name__ == "__main__" :
   word=blog.set("}egassem_terces_ym_edoced_uoy_did_woh{ftca",1)
   solve(word)