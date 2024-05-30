import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
#python
def solve(s):
  print(s[::-1])
if __name__ == "__main__" :
  s=blog.set("MELBORP_A_EVLOS_OT_SDRAWKCAB_GNIKROW",1) 
  solve(s)