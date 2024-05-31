from pwn import *
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
# needed for the xor()
def solve(a,b,type="hex"):
 a = bytes.fromhex(a)
 b = bytes.fromhex(b)
 s=xor(a, b)
 if type=="hex":
  return s.hex()
 else:
   return s.decode()     
if __name__ == "__main__" :
 a=blog.set("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313",1)
 b=blog.set("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e",2)
 type=blog.set("hex",3)    
 print(solve(a,b,type) )