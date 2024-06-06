def add_round_key(s, k):
  s = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]
  x= [ [-1]*len(s) for i in range(len(s))]
  i=0
  c=len(s)
  for i in range(c):
   for j in range(c):
     if x[i][j]==-1 :
       x[i][j]=s[i][j]^k[i][j]
  return x      
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
if __name__ == "__main__" :
 state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]
 round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
 state=blog.set(state,1)
 round_key=blog.set(round_key,2) 
 operation=blog.set("byte",3)
 x=add_round_key(state, round_key)
 if operation=="byte":
  print(blog.solveup("matrix","matrixtobyte",x))