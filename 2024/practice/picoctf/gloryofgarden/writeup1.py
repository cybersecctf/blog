import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import os
def solve(file,search="pico"):
       os.system(f"strings {file}|grep={search}")
if __name__ == "__main__" :
  solve("garden.jpg")