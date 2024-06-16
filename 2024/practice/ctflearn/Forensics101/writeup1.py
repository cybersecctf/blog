
#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
#python
import subprocess,os

def solve(file, search=""):
    result=""
    if search!="":       
        result = subprocess.run(f"strings {file} | grep {search}", shell=True, text=True, capture_output=True)
    else:
           result = subprocess.run(f"strings {file}", shell=True, text=True, capture_output=True)          
    return result.stdout

if __name__ == "__main__":
    file=blog.set("file.jpg",1)
    search=blog.set("{",2)  #flag have '{' normally    
    print("d",solve("file.jpg", search))
