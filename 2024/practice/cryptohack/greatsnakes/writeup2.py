#python
import sys
# import this

import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(d,search="crypto",i1=300):
 ords=d 
 s=""
 if not "[" in ords and  isinstance(ords, str):
   s=[]         
   for x in ords:
     s.append(ord(x))
   ords=s
 print(s)
 
 for i in range(i1):
 
  s="".join(chr(o ^ i) for o in ords)
  if search in s:
   print("Here is your flag:")
   print(f"xor of {d} and {hex(i)} is {s}")
if __name__ == "__main__" :
 ords=blog.set([81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79],1)
 search=blog.set("crypto",2);
 solve("da","DA",0x23)