
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def solve(file, search=""):
    result=""
    if search!="":       
        result = subprocess.run(f"strings {file} | grep {search}", shell=True, text=True, capture_output=True)
    else:
           result = subprocess.run(f"strings {file}", shell=True, text=True, capture_output=True)          
    return result.stdout

if __name__ == "__main__" :
  print(solve("garden.jpg"))
