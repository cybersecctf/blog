
#python

import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
import sys

def solve(ords,hexs,search="crypto"):
 if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3. or use $python3 if have")
    exit(0) 
 print("Here is your flag:")
 if hexs=="":
    hexs="0x0"#handle empty hexs
 hexs = int(hexs, 16) 
 print("".join(chr(o ^ hexs) for o in ords))

if __name__ == "__main__" :
   ords=blog.set("[81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]",1)
   hexs=blog.set("0x32",2)
   solve(ords,hexs)
