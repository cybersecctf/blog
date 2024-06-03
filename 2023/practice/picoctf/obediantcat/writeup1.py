import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import os
def solve(file="flag.txt"):
  os.system(f"strings {file}");
if __name__ == "__main__" :
  solve()