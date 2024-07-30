
#python
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import binascii 
def solve(operation, hexs): 
  if operation=="decode":
    return bytes.fromhex(hexs).decode('utf-8')
  if operation=="encode":
    return binascii.hexlify(hexs.encode('utf-8')).decode('utf-8')
    
if __name__ == "__main__" :
 hex=blog.set("54776f206d6f7265",1)
 print(solve("decode",hex))
