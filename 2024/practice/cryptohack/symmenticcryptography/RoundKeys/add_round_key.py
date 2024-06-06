from pwn import *
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


def add_round_key(s, k,row=4):
  s = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]
  x= [ [-1]*len(s) for i in range(len(s))]
  i=0
  for i in range(row):
   for j in range(row):
     if x[i][j]==-1 :
       x[i][j]=s[i][j]^k[i][j]
  return x     
        
               

import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
x=add_round_key(state, round_key)
print(blog.solveup("matrix","matrixtobyte",x))