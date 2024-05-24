#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(hex): 
   return bytes.fromhex(hex)
if __name__ == "__main__" :
 hex=blog.set("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d",1)
 print(solve(hex))