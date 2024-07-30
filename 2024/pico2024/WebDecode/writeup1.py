
import base64
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(operation,a): 
 try:
  if operation=="decode":
    return base64.b64decode(a)
  else:
    return base64.b64encode(a)
 except Exception as e:
  return f"not a base64 nymber {str(e)}"
if __name__ == "__main__" :
  a=blog.set("cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9",1)
  print(solve("decode",a)) 
