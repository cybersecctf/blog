#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(s,n):
 try:
  ords=blog.solveup("encode/decode full","encode",s,"ascii") 
  hexs = hex(int(n))
  hexs=int(hexs,16)
  print("".join(chr(o ^ hexs) for o in ords))
 except Exception as e:
   print(str(e))
if __name__ == "__main__" :
 s =blog.set("label",1)
 n =blog.set(13,2)
  
 solve(s,n)