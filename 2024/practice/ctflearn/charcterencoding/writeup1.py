
#python
#usage -v  hexnumbers [hex/base64 default hex]
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import base64

from binascii import unhexlify

def solve(s,type):
 if " " in s:
  s=s.replace(" ","")

 if "0x" in s:
  s=s.replace("0x","")
 result = unhexlify(s)
 if type=='base64':
  result = base64.b64encode(result)
 return result
if __name__ == "__main__" :
 s=blog.set('41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D',1)
 type=blog.set('hex',2)
 print(solve(s,type))

