
#python
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

def solve(v1,v2):
 v3=v1^v2
 v4="hex"
 if len(sys.argv)>3:
  v4=sys.argv[3]
 if v4!="hex":
   return v3
 else :
   return hex(v3)
if __name__ == "__main__" :
 v1=blog.set(0xc4115,1) 
 v2=blog.set(0x4cf8,2)
 print(solve(v1,v2))
