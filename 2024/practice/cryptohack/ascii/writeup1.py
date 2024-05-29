#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(nums,sep=""):
  if   sep!="":
    nums = [int(i) for i in nums.split(sep)] 
  print("".join((chr(o) for o in nums)))
if __name__ == "__main__" :
  
  nums=blog.set([99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125],1)
  solve(nums)