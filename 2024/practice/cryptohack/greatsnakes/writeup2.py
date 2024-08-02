
#python
import sys
# import this

import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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
 solve("\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e","ctflearn")
