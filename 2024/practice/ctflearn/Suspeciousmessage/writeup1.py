
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(inspecturl="http://rumkin.com/tools/cipher/playfair.php"):
  blog.solveup("inspect",inspecturl)
  blog.solveup("inspect","https://cybersecctf.github.io/blog/2024/practice/ctflearn/Suspeciousmessage/site.png")
if __name__ == "__main__" :
 solve()
